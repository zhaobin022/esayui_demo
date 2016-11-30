__author__ = 'zhaobin022'
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os
import json
from Model.User import UserService
import BootMapper

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('index.html')

    def post(self, *args, **kwargs):

        user_service = UserService()
        user_list = user_service.get_user_list()
        print user_list

        self.write(json.dumps(user_list))


class GetUserHandler(tornado.web.RequestHandler):
    def get(self):
        user_service = UserService()
        user_list = user_service.get_user_list()

        self.write(json.dumps(user_list))

    def post(self):
        user_service = UserService()
        user_list = user_service.get_user_list()

        self.write(json.dumps(user_list))



class SaveUserHandler(tornado.web.RequestHandler):
    def post(self):
        '''
        firstname,lastname,phone,email
        :return:
        '''
        '''
        :return:
        '''
        firstname = self.get_argument('firstname')
        lastname = self.get_argument('lastname')
        phone = self.get_argument('phone')
        email = self.get_argument('email')

        user_service = UserService()
        user_service.insert_into_user(firstname,lastname,phone,email)
        ret = {
            'errorMsg':False
        }
        self.write(json.dumps(ret))



class DeleteUserHandler(tornado.web.RequestHandler):
    def post(self):
        '''
        firstname,lastname,phone,email
        :return:
        '''
        id = self.get_argument('id')

        user_service = UserService()
        user_service.delete_user_by_id(id)

        ret = {
            'success':True
        }
        self.write(json.dumps(ret))

class UpdateUserHandler(tornado.web.RequestHandler):
    def post(self):
        '''
        firstname,lastname,phone,email
        :return:
        '''
        id = self.get_argument('id')
        firstname = self.get_argument('firstname')
        lastname = self.get_argument('lastname')
        phone = self.get_argument('phone')
        email = self.get_argument('email')


        user_service = UserService()
        user_service.update_user_by_id(id,firstname,lastname,phone,email)

        ret = {
            'errorMsg':False
        }
        self.write(json.dumps(ret))







settings = {
    'template_path': 'template',
    'static_path': 'statics',
    'static_url_prefix': '/statics/',
}

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/get_users", GetUserHandler),
    (r"/save_user", SaveUserHandler),
    (r"/delete_user", DeleteUserHandler),
    (r"/update_user", UpdateUserHandler),


], **settings)


if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
