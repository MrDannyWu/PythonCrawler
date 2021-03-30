# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           mysql_client.py
   Description:    MySQL数据库工具类封装
   Author:
   Create Date:    2020/03/24
-------------------------------------------------
   Modify:
                   2020/03/24:
-------------------------------------------------
"""
import pymysql
from pymysql import connect as conn
from utils.log_handler import LogHandler

class MySQLClient(object):
    def __init__(self, db_host, db_user, db_password, db_name, db_port, cursorclass=pymysql.cursors.DictCursor, **kwargs):
        """
        连接数据库方法
        :param db_host: MySQL数据库所在的主机
        :param db_user: 用户名
        :param db_pass: 密码
        :param database: 要连接的数据库
        :param db_port: MySQL数据库的端口
        :return: 连接对象
        """
        self.log = LogHandler('db')
        try:
            self.__connect = conn(host=db_host, user=db_user, password=db_password, db=db_name, port=db_port,cursorclass=cursorclass, **kwargs)
            self.__cursor = self.__connect.cursor()
        except Exception as e:
            self.log.info('数据库链接失败: ' + str(e))

    def get_connect(self):
        # 获取连接
        return self.__connect

    def get_cursor(self):
        # 获取游标
        return self.__cursor

    def commit(self):
        # 提交事务
        self.__connect.commit()

    def close(self):
        """
        关闭游标对象和连接对象
        """
        try:
            if self.__cursor != None:
                self.__cursor.close()
            if self.__connect != None:
                self.__connect.close()
        except Exception as e:
            self.log.info('数据库关闭失败: ' + str(e))
        return True

    def __edit(self, sql, params):
        """
        执行增删改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        """
        count = 0
        try:
            count = self.__cursor.execute(sql, params)
            self.__connect.commit()
        except Exception as e:
            self.log.info('数据库操作失败: ' + str(e))
        return count

    def update(self, sql, params=None):
        '''
        执行修改
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__edit(sql, params)

    def insert_one(self, sql, params=None):
        '''
        执行新增
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__edit(sql, params)

    def insert_many(self, sql, params):
        """
        一次插入多条数据
        :param sql:
        :param values:
        :return:
        """
        try:
            self.__cursor.executemany(sql, params)
            self.__connect.commit()
        except Exception as e:
            self.log.info('插入多条数据失败: ' + str(e))

    def delete(self, sql, params=None):
        '''
        执行删除
        :param sql: sql语句
        :param params: sql语句对象的参数列表，默认值为None
        :return: 受影响的行数
        '''
        return self.__edit(sql, params)


    def fetch_count(self, sql, params=None):
        """
        查询一共有多少条数据
        :param connect:
        :param sql:
        :return:
        """
        data_count = -1
        try:
            data_count = self.__cursor.execute(sql, params)
        except Exception as e:
            self.log.info('查询数据总量错误: ' + str(e))
        return data_count

    def fetch_all(self, sql, params=None):
        """
        查询所有结果
        :param connect:
        :param sql:
        :return:
        """
        data_list = []
        try:
            count = self.__cursor.execute(sql, params)
            if count != 0:
                data_list = self.__cursor.fetchall()
            return data_list
        except Exception as e:
            self.log.info('查询失败: ' + str(e))
            return None


    def fetch_one(self, sql, params=None):
        """
        查询所有结果
        :param connect:
        :param sql:
        :return:
        """
        data_list = []
        try:
            count = self.__cursor.execute(sql, params)
            if count != 0:
                data_list = self.__cursor.fetchone()
        except Exception as e:
            self.log.info('查询失败: ' + str(e))
        return data_list

    def fetch_all_table_field(self, table_name, params=None):
        """
        获取表的所有字段
        :param table_name:
        :param params:
        :return:
        """
        sql = 'show full columns from {}'.format(table_name)
        field_list = self.fetch_all(sql, params=params)

        table_field = {}
        for j in field_list:
            field_name = j[0]
            field_type = j[1]

            table_field[field_name] = field_type

        return table_field

    def fetch_all_table_name(self, params=None):
        """
        获取数据库里的所有表名
        :param params:
        :return:
        """
        results = self.fetch_all('show tables', params=params)
        table_name_list = []
        for i in results:
            table_name_list.append(i[0])

        return table_name_list


if __name__ == '__main__':
    pass