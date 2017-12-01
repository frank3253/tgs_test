import configparser

import os, sys


# 用configparser类读取ini文件，提供一个通用获取配置文件内部参数的方法
def getconfig(section, key):
    path = os.path.abspath(os.path.dirname(__file__) + '/' + '../../../' + 'config')
    filename = path + "\\config.ini"
    config = configparser.ConfigParser( )
    config.read(filename)
    return config.get(section, key)


# 获取用户数据
def getuser():
    username = getconfig("user", "username")
    userpassword = getconfig("user", "password")
    return username, userpassword


def emailconfig():
    emailname = getconfig("email", "username")
    emailpassword = getconfig("email", "password")
    emailto = getconfig("email", "to")
    return emailname, emailpassword, emailto


def dbconfig():
    dbuser = getconfig("mysql", "username")
    dbpassword = getconfig("mysql", "password")
    return dbuser, dbpassword


# 自测
# if __name__ == "__main__":
    # name = getuser( )[0]
    # password = getuser( )[1]
    # print(name, password)
    # name = emailconfig( )[0]
    # password = emailconfig( )[1]
    # to = emailconfig()[2]
    # print(name, password, to)
    # name = dbconfig( )[0]
    # password = dbconfig( )[1]
    # print(name, password)
