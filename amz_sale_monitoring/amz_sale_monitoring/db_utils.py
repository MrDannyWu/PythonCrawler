from pymysql import connect as conn


def connect_db(db_host, db_user, db_pass, database, db_port):
    """
    连接数据库方法
    :param db_host: MySQL数据库所在的主机
    :param db_user: 用户名
    :param db_pass: 密码
    :param database: 要连接的数据库
    :param db_port: MySQL数据库的端口
    :return: 连接对象
    """
    try:
        connect = conn(host=db_host, user=db_user, password=db_pass, db=database, port=db_port)
        return connect
    except:
        pass
    print('数据库连接成功: ', connect)


def query_data(connect, sql):
    """
    查询数据的方法
    :param connect: 数据库连接对象
    :param sql: 要执行的查询语句
    :return: 查询结果集
    """
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except:
        pass


def insert_update_drop_data(connect, sql, print_info=None):
    """
    插入、删除、更新数据的统一方法
    :param connect: 数据库连接对象
    :param sql: 要执行的sql语句
    :param print_info: 打印sql语句执行成功信息
    :return: None
    """
    try:
        cursor = connect.cursor()
        cursor.execute(sql)
        connect.commit()
    except:
        pass
    # print(print_info)


def query_results(connect, sql):
    """
    查询数据库中符合条件的有多少条记录，以及查询结果
    :param connect: 数据库连接对象
    :param sql: 要执行的sql语句
    :return: 返回查询记录条数以及查询结果
    """
    try:
        cursor = connect.cursor()
        result = cursor.execute(sql)
        results = cursor.fetchall()
        return [result, results]
    except:
        pass
