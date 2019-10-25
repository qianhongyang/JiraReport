from configparser import ConfigParser
import os

nowpath = os.path.dirname(os.path.abspath(__file__))         # 获取当前文件所在目录的上一级目录
path = os.path.join(nowpath, "config.ini")


def readconfig(secname="JIRA", option="JVERSION"):

    cf = ConfigParser()
    cf.read(path)                     # 拼接得到config.ini文件的路径，直接使用
    result = cf.get(secname, option)  # 获取对应的值
    return result

