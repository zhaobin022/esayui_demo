#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer, Integer, CHAR, VARCHAR, ForeignKey, Index, DateTime, DECIMAL, TEXT
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import Config


engine = create_engine(
    "mysql+pymysql://%s:%s@%s:%d/%s?%s" % (
        Config.PY_MYSQL_CONN_DICT['user'],
        Config.PY_MYSQL_CONN_DICT['passwd'],
        Config.PY_MYSQL_CONN_DICT['host'],
        Config.PY_MYSQL_CONN_DICT['port'],
        Config.PY_MYSQL_CONN_DICT['db'],
        Config.PY_MYSQL_CONN_DICT['charset'],
    ) ,
    max_overflow=5,
    echo=True
)

Base = declarative_base()



class UserInfo(Base):
    """
    用户信息
    """

    __tablename__ = 'userinfo'

    id = Column(Integer, primary_key=True)
    firstname = Column(VARCHAR(64))
    lastname = Column(VARCHAR(64))
    phone = Column(VARCHAR(64))
    email = Column(VARCHAR(64))




def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

drop_db()
init_db()