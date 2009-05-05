#coding=utf8
import logging.config
import os

from com.youmogan.spider import YMG_CONF_DIR
from com.youmogan.spider import YMG_OUT_SOURCE
from com.youmogan.spider import YMG_OUT_TEXT
from datetime import date
__author__ = "jun.yanj"
__date__ = "$2008-11-25 10:44:22$"

## initialize logging
#logging.config.fileConfig(YMG_CONF_DIR + os.path.sep + 'logging.conf')
#today = date.today()
#
## today pattern
#list_url = r'http://www.haha365.com/xd_joke/index.htm'
#pattern_title = r'<TD  valigN=botTom height="57" ClaSS="L26">(.*?)</TD>'
#pattern_body = r'<tD valign=top id=fontZooM clAss="L17" height=76>(.*?)</Td>'
#site_name = 'haha365'
#out_source_dir_ = YMG_OUT_SOURCE + os.path.sep + str(today) + os.path.sep + site_name + os.path.sep
#out_text_dir_ = YMG_OUT_TEXT + os.path.sep + str(today) + os.path.sep + site_name + os.path.sep
#_out_text_dir_ = YMG_OUT_TEXT + os.path.sep + '2008-11-25' + os.path.sep + site_name + os.path.sep

if __name__ == "__main__":
    print "Hello";