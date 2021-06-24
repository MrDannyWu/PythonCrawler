from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql
import datetime


def query_dayly_product(sql):
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()

    cursor.execute(sql)
    results_1 = cursor.fetchall()
    print(len(results_1))
    return results_1


def update_db():
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    query_sql = 'SELECT id FROM amz_product WHERE error = "yes"'
    cursor.execute(query_sql)
    results = cursor.fetchall()
    for i in results:
        print(i[0])
        update_sql = 'update amz_product set error="no" where id={}'.format(i[0])
        cursor.execute(update_sql)
        connect.commit()
    print(len(results))


def query_product():
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    # query_all_sql = 'select * from product where class_id = 6768 and asin = "B004O290TW"'
    # query_all_sql = 'select * from amz_product where error = "yes"'
    query_all_sql = 'select asin from amz_product where error != "404"'
    cursor.execute(query_all_sql)
    results = cursor.fetchall()
    print(len(results))

    query_all_sql_1 = 'select product_asin from amz_product_details where report_time = "2019-09-16"'
    cursor.execute(query_all_sql_1)
    results_1 = cursor.fetchall()
    # print(len(results))
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    e_list = []
    for x in results:
        print(x[0])
        b_list.append(x[0])
    for y in results_1:
        print(y[0])
        c_list.append(y[0])
    print(len(b_list))
    print(len(c_list))
    for i in b_list:
        # if c_list.count(i) > 1:
        #     d_list.append(i)
        if i not in c_list:
            a_list.append(i)
            print(i)
    # print(len(a_list))
    # print(a_list)
    # print(len(list(set(c_list))))
    # print(set(c_list))
    # print('d_list: ', len(list(set(d_list))))
    # print(list(set(d_list)))
    print(a_list)
    print(len(a_list))


def update_db():
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    query_sql = 'SELECT id FROM amz_product WHERE error = "yes"'
    cursor.execute(query_sql)
    results = cursor.fetchall()
    for i in results:
        print(i[0])
        update_sql = 'update amz_product set error="no" where id={}'.format(i[0])
        cursor.execute(update_sql)
        connect.commit()
    print(len(results))


def main():
    # query_product()
    today_time = datetime.datetime.now().strftime('%Y-%m-%d')
    sql = 'select id from amz_product'
    query_sql = 'select asin from amz_product where error != "404"'
    query_sql_1 = 'select asin from amz_product where error = "no"'
    sql_1 = 'select product_asin from amz_product_details where report_time = "{}"'.format(today_time)
    # sql_1 = 'select product_asin from amz_product_details where report_time = "2019-10-03"'
    sql_2 = 'SELECT id FROM `amz_product` where error ="yes"'

    query_dayly_product(sql)
    query_dayly_product(query_sql)
    query_dayly_product(query_sql_1)
    query_dayly_product(sql_1)
    query_dayly_product(sql_2)

    # sql_2 = 'select product_asin from amz_product_details where report_time = "2019-09-12"'
    # sql_3 = 'select product_asin from amz_product_details where report_time = "2019-09-13"'
    # res_1 = query_dayly_product(sql_2)
    # res_2 = query_dayly_product(sql_3)
    # asin1_list = []
    # asin2_list = []
    # asin3_list = []
    # for i in res_1:
    #     asin1_list.append(i[0])
    # for j in res_2:
    #     asin2_list.append(j[0])
    # for x in asin1_list:
    #     if x not in asin2_list:
    #         asin3_list.append(x)
    # print(asin3_list)
    # print(len(asin3_list))
    # asin_tuple = tuple(asin3_list)
    # qsql = 'select * from amz_product_details where report_time = "2019-09-12" and product_asin in {}'.format(asin_tuple)
    # resu_1 = query_dayly_product(qsql)
    # for k in resu_1:
    #
    #     print(k)
    # update_db()


if __name__ == '__main__':
    main()