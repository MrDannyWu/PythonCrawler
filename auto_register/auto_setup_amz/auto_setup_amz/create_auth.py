from auto_setup_amz.db_utils import *
from auto_setup_amz.db import *
import random
import string


def generate_random_str(randomlength):
    """
    string.digits = 0123456789
    string.ascii_letters = 26
    """

    print(string.digits)
    print(string.ascii_letters)
    str_list = random.sample(string.digits + string.ascii_letters, randomlength)
    print(str_list)
    random_str = ''.join(str_list)
    return random_str.upper()


connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
for i in range(100):
    auth_code = generate_random_str(randomlength=25)
    print(auth_code)
    insert_sql = 'insert into auth (auth_code) values("{}")'.format(auth_code)
    insert_update_drop_data(connect, insert_sql, '')