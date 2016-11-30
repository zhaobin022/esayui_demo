#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.DI import MetaClass


class IUserRepository:

    def insert_user(self,firstname, lastname,phone,email):
        """
        获取所有的省份个数
        :return:
        """
        raise Exception()


    def get_user_by_id(self,user_id):
        raise Exception()

    def get_user_list(self):
        raise Exception()


    def delete_user_by_id(self,user_id):
        raise Exception()


    def update_user_by_id(self,id,firstname, lastname,phone,email):
        raise Exception()

class User:

    def __init__(self, firstname, lastname,phone,email):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.email = email

class UserService:
    __metaclass__ = MetaClass

    def __init__(self, user_repository):
        self.userRepository = user_repository

    def insert_into_user(self, firstname, lastname,phone,email):
        self.userRepository.insert_user(firstname, lastname,phone,email)

    def get_user_by_id(self,user_id):
        user_obj = self.userRepository.get_user_by_id(user_id)
        return user_obj

    def get_user_list(self):
        user_list = self.userRepository.get_user_list()
        return user_list


    def delete_user_by_id(self,user_id):
        m = self.userRepository.delete_user_by_id(user_id)

    def update_user_by_id(self,id,firstname, lastname,phone,email):
        self.userRepository.update_user_by_id(id,firstname, lastname,phone,email)