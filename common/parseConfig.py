# -*- coding: utf-8 -*-
'''
@File  : parseConfig.py
@Date  : 2019/1/15/015 16:34
'''
from configparser import ConfigParser
import os, platform


# 设置路径
def setPath(pathName=None, fileName=None):
    oldPath = os.path.dirname(__file__)
    if pathName is not None:
        newPath = oldPath.replace("common", pathName)
        if fileName is not None:
            if platform.system() is "Windows":
                path = "{}\{}".format(newPath, fileName)
            else:
                path = "{}/{}".format(newPath, fileName)
        else:
            path = newPath
    else:
        path = oldPath
    return path


class ParseConfig(object):
    def __init__(self):
        # 配置文件所在路径
        path = setPath(pathName="config", fileName="info.ini")
        self.cf = ConfigParser()
        self.cf.read(path, encoding="utf8")

    # 根据section读取配置文件信息，返回数据字典
    def get_info(self, section):
        info = {}
        for i in self.cf.options(section):
            info[i] = self.cf.get(section, i)
        return info

    def get_report_info(self):
        return self.cf.options("report")


if __name__ == '__main__':
    pc = ParseConfig()
    rp=str(pc.get_info("report")["colname"])
    hh=rp.split(",")
    print(hh)
