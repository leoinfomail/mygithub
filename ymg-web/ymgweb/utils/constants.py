#coding=utf8
"""
这里记录的是业务模型，业务逻辑上的常量，最好和应用本身设置无关
"""
__author__="jun.yanj"
__date__ ="$2008-12-30 23:40:06$"



class ContentType(object):
    HUMOR = 10000
    HUMOR_MAX = 19999
    IQ = 20000
    IQ_MAX = 29999
    RIDDLE = 30000
    RIDDLE_MAX = 39999
    def __init__(self):
        pass

content_type = ContentType()

class Size(object):
    DEFAULT_LIST = 10
    DEFAULT_MANAGE_LIST = 50
    def __init__(self):
        pass

size = Size()