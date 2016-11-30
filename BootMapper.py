#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.DI import Mapper
from Model.User import UserService
from Repository.UserRepository import UserRepository
#
Mapper.register(UserService, UserRepository())