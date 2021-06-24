import pandas as pd
from amz_product_info.db import *
from amz_product_info.db_utils import *
import datetime

update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
df = pd.DataFrame()
results = pd.read_excel('data.xlsx')
# print(results)
conn = connect_db(DB_HOST_1, DB_USER_1, DB_PASS_1, DATABASE_1, DB_PORT_1)
base_host = 'https://www.amazon.'
for asin, site, sku, account in zip(results['Asin'], results['站点'], results['sku'], results['账号']):
    # if asin[0] != 'X' and site.lower() in ['us', 'uk', 'de', 'it', 'es']:
    if asin[0] != 'X':
        if site.lower() == 'uk' or site.lower() == 'jp':
            domain = 'co.{}/'.format(site.lower())
        elif site.lower() == 'ae' or site.lower() == 'ca' or site.lower() == 'de' or site.lower() == 'es' or site.lower() == 'in' or site.lower() == 'it':
            domain = '{}/'.format(site.lower())
        elif site.lower() == 'au' or site.lower() == 'mx':
            domain = 'com.{}/'.format(site.lower())
        elif site.lower() == 'us':
            domain = 'com/'
        product_url = base_host + domain + 'dp/{}/'.format(asin)
        print(asin, site)
        print(product_url)

        query_sql = 'select id from amz_product_url where product_url = "{}"'.format(product_url)
        print(query_sql)
        query_result = query_results(conn, query_sql)
        print(query_result)
        if query_result[0] == 0:
            insert_sql = 'insert into amz_product_url(asin, site, product_url, update_time, error, sku, account)VALUES ("{}", "{}", "{}", "{}", "{}"), "{}", "{}")'.format(asin, site.lower(), product_url, update_time, 'no', sku, account)
            insert_update_drop_data(conn, insert_sql, '')
        else:
            update_sql = 'update amz_product_url set asin="{}", site="{}", product_url="{}", update_time="{}", error="{}", sku="{}", account="{}" where product_url="{}"'.format(asin, site.lower(), product_url, update_time, 'no', sku, account, product_url)
            insert_update_drop_data(conn, update_sql, '')
print(len(results['Asin']))
print(len(results['站点']))
print(list(set(results['站点'])))
