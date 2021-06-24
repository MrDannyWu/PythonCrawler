from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql


def quchong():

    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    # 查询重复的
    sql = 'select id from amz_product_details where report_time="2019-09-05" group by product_asin having count(1)>1'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(len(results))
    # for i in results:
    #     id_num = i[0]
    #     delete_sql = 'delete from amz_product_details where id = id_num'
    #     cursor.execute(delete_sql)
    #     connect.commit()
    #     print(id_num, '已去重。。。')


def main():
    quchong()
    # update_db()


if __name__ == '__main__':
    main()
