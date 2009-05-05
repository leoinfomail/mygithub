#coding=utf8
import logging.config
import os
import re

from com.youmogan.spider import YMG_CONF_DIR
from com.youmogan.spider import YMG_OUT_SOURCE
from com.youmogan.spider import YMG_OUT_TEXT
from com.youmogan.spider.source_getter import HtmlSourceGetter
from datetime import date

# initialize logging
logging.config.fileConfig(YMG_CONF_DIR + os.path.sep + 'logging.conf')
today = date.today()

# --------------------------------------------------------------------------------------
# today pattern
pattern_title = r'<TD  valigN=botTom height="57" ClaSS="L26">(.*?)</TD>'
pattern_body = r'<tD valign=top id=fontZooM clAss="L17" height=76>(.*?)</Td>'
site_name = 'oicqiq'
out_source_dir_ = YMG_OUT_SOURCE + os.path.sep + str(today) + os.path.sep + site_name + os.path.sep
out_text_dir_ = YMG_OUT_TEXT + os.path.sep + str(today) + os.path.sep + site_name + os.path.sep

# miyumiyu
out_source_dir = YMG_OUT_SOURCE + os.path.sep + str(today) + os.path.sep + 'miyumiyu' + os.path.sep
out_text_dir = YMG_OUT_TEXT + os.path.sep + '2009-01-01' + os.path.sep + 'miyumiyu' + os.path.sep
# --------------------------------------------------------------------------------------

coding = ['gbk', 'gb2312', 'gb18030']

# 变化点之一：提供可供解析的url list
def get_url_list():
    """
    对外提供url list，形式为(url_list, coding)
    """
#    return get_haha365_urls()
#    return get_miyumiyu_urls()
    return get_oicq_iq_urls()

def get_haha365_urls():
    list_url = r'http://www.haha365.com/xd_joke/index.htm'
    base_url = r'http://www.haha365.com'
    getter = HtmlSourceGetter()
    html_data = getter.get_uniform_html_source(list_url, coding[1])
    pattern = r'<img src="/Pic/02.gif"><a Class="" target="_blank"  href="(.*?)" >'
    uris = re.findall(pattern, html_data['data'])
    result_urls = []
    for uri in uris:
        result_urls.append(base_url + uri)
    return (result_urls, coding[1])

def get_miyumiyu_urls():
    """英语的没做，090102"""
    result_urls = [
    r'http://www.miyumiyu.cn/zimi/',
    r'http://www.miyumiyu.cn/zimi/5.html',
    r'http://www.miyumiyu.cn/dengmi/',
    r'http://www.miyumiyu.cn/dengmi/',
    r'http://www.miyumiyu.cn/gaoxiao/',
    r'http://www.miyumiyu.cn/english/',
    r'http://www.miyumiyu.cn/love/',
    r'http://www.miyumiyu.cn/chengren/',
    ]
    return (result_urls, coding[1])

def get_oicq_iq_urls():
    base = r'http://www.oicq88.com/iq/'
    result_urls = []
    i_list = [35, 11, 29, 30, 31, 32, 35, 38, 43, 44, 45, 113, 148]
    for i in i_list:
        if i < 10:
            i = '0' + str(i)
        result_urls.append(base + str(i) + r'.htm')
    return (result_urls, coding[1])

if __name__ == "__main__":
#    url = r'http://www.haha365.com/xd_joke/index.htm'
#    print get_haha365_urls(url)
    get_oicq_iq_urls()
    print 'done'
    