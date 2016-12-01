#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Model.User import IUserRepository
from Repository.DbConnection import DbConnection
import logging
import os



class UserRepository(IUserRepository):

    def __init__(self):
        self.db_conn = DbConnection()

    def insert_user(self,firstname,lastname,phone,email):
        cursor = self.db_conn.connect()
        sql = """insert into userinfo(firstname,lastname,phone,email) values(%s,%s,%s,%s)"""
        ret = cursor.execute(sql, (firstname, lastname,phone,email))
        print ret
        self.db_conn.close()


    def get_user_by_id(self,user_id):
        cursor = self.db_conn.connect()
        sql = """select * from userinfo where id = %s """
        print type(user_id)
        cursor.execute(sql, (user_id,))
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result

    def get_user_list(self):
        cursor = self.db_conn.connect()
        sql = """select * from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result


    def delete_user_by_id(self,user_id):
        cursor = self.db_conn.connect()
        sql = """delete from userinfo where id = %s """
        db_result = cursor.execute(sql, (user_id,))
        self.db_conn.close()

        return db_result

    def update_user_by_id(self,id,firstname, lastname,phone,email):
        cursor = self.db_conn.connect()
        sql = """update userinfo set firstname=%s, lastname=%s,phone=%s,email=%s where id = %s """
        db_result = cursor.execute(sql, (firstname, lastname,phone,email,id))
        self.db_conn.close()

        return db_result

    def get_user_list_by_page(self,page,page_size):


        start = (int(page)-1)*int(page_size)

        cursor = self.db_conn.connect()
        sql = """select * from userinfo limit %s,%s"""
        print sql
        print start,page_size
        cursor.execute(sql,(int(start),int(page_size)))
        db_result = cursor.fetchall()
        self.db_conn.close()
        return db_result

    def get_user_count(self):
        cursor = self.db_conn.connect()
        sql = """select count(*) as count from userinfo"""
        cursor.execute(sql)
        db_result = cursor.fetchone()
        self.db_conn.close()

        return db_result
