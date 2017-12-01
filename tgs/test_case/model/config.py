import configparser

# 用configparser类读取ini文件，提供一个通用获取配置文件内部参数的方法
def getconfig(section, key):
    filename = "D:/py3/webtest/config/config.ini"
    config = configparser.ConfigParser( )
    config.read(filename)
    return  config.get(section, key)

# 获取用户数据
def getuser():
    username = getconfig("user","username")
    password = getconfig("user","password")
    return username, password

# 自测
# if __name__ == "__main__":
#      name = getuser()[0]
#      password = getuser()[1]
#      print(name,password)
