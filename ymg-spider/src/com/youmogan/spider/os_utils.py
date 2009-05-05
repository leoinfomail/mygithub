#coding=utf8
import os
from os.path import isdir

__author__ = "jun.yanj"
__date__ = "$2008-11-20 21:57:01$"

def create_dir(path):
    """创建目录，已经存在视为成功。path有没有最后的pathsep没有关系"""
    if not isdir(path):
        os.makedirs(path)

def create_file_name(today, name='', index=1, postfix='.txt'):
    """创建文件名：日期-[名称-]num[.后缀]"""
    if 0 < index < 10:
        index_str = '00' + str(index)
    elif index < 100:
        index_str = '0' + str(index)
    else:
        index_str = str(index)
    if name:
        return str(today) + '-' + name + '-' + index_str + postfix
    return str(today) + '-' + index_str + postfix

if __name__ == "__main__":
    create_dir('d:\\abc\\d')
    print "Hello";