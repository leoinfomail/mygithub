#coding=utf8
import re
from glob import glob
from time import time

from com.youmogan.spider.digester import Digester
from com.youmogan.spider.os_utils import create_dir
from com.youmogan.spider.os_utils import create_file_name
from com.youmogan.spider.source_getter import HtmlSourceGetter
from com.youmogan.spider.url_generater import get_url_list
from com.youmogan.spider.url_generater import out_source_dir_
from com.youmogan.spider.url_generater import out_text_dir_
from com.youmogan.spider.url_generater import pattern_body
from com.youmogan.spider.url_generater import pattern_title
from com.youmogan.spider.url_generater import site_name
from com.youmogan.spider.url_generater import today

def get_raw_html():
    """第一步，取得统一编码的源文件到本地目录下"""
    getter = HtmlSourceGetter()
    (urls, coding) = get_url_list()
    # get data
    html_data = {}
    for url in urls:
        html_data[url] = getter.get_uniform_html_source(url, coding)
    # output raw data
    create_dir(out_source_dir_)
    i = 0
    for url, raw_data in html_data.items():
        if not raw_data['data']:
            continue
        raw_file = open(out_source_dir_ + create_file_name(today, site_name, i + 1, '.ymg_html'), 'w')
        raw_file.write(raw_data['request_url'])
        raw_file.write(u'\n\n')
        raw_file.write(raw_data['data'].replace('\r\n', ''))
        raw_file.close()
        i += 1
    return i

def digest_data():
    create_dir(out_text_dir_)
    file_out_text = open(out_text_dir_ + create_file_name(today, site_name, postfix='.txt'), 'w')
    dg = Digester()
    j = 0
    for file in glob(out_source_dir_ + '*.ymg_html'):
        raw_file = open(file, 'r')
        data = raw_file.read()
        raw_file.close()
        title = dg.search_one_result(pattern_title, data, 1)
        body = dg.search_one_result(pattern_body, data, 1)
        title = dg.regularize_content(title)
        body = dg.regularize_content(body)
        if title and body:
            file_out_text.write('--ymg-humor--\n')
            file_out_text.write(title + '\n')
            file_out_text.write(body + '\n')
            j += 1
    file_out_text.close()
    return j

def digest_oicq_iq():
    create_dir(out_text_dir_)
    file_out_text = open(out_text_dir_ + create_file_name(today, site_name, postfix='.txt'), 'w')
    pattern_que = r'>(\d*?):(.*?)</[tT][dD]>'
    pattern_ans = r'get(\d*?)(.*?)答案：(.*?)\\n\\n版权所有'
    j = 0
    digested_data = []
    for file in glob(out_source_dir_ + '*.ymg_html'):
        raw_file = open(file, 'r')
        data = raw_file.read()
        data = data.decode('gbk').encode('utf-8')
        raw_file.close()
        que_list = re.findall(pattern_que, data, re.DOTALL)
        que_dg_list = []
        for (index, que) in que_list:
            que_dg_list.append(que.strip())
            #file_out_text.write(index + '\n' + que + '\n')
            #file_out_text.flush()
        ans_list  = re.findall(pattern_ans, data, re.DOTALL)
        ans_dg_list = []
        for (index1, other1, ans) in ans_list:
            ans_dg_list.append(ans.strip())
            #file_out_text.write(index1 + '\n' + data1 + '\n')
            #file_out_text.flush()
        try:
            for i in range(len(que_list)):
                digested_data.append((que_dg_list[i], ans_dg_list[i]))
        except Exception:
            print i
            print que_dg_list[i]
            print raw_file.name
    for (subject, content) in digested_data:
        if subject and content:
            file_out_text.write('--ymg-iq--\n')
            file_out_text.write('<p>' + subject + '</p>' + '\n')
            file_out_text.write('<p>' + content + '</p>' + '\n')
            j += 1
    file_out_text.close()
    return j

def view_result():
    """
    读取经过处理的xml文件。比如自动上传。
    """
    for file in glob(out_text_dir_ + '*.txt'):
        dg_file = open(file, 'r')
        print dg_file.read()

if __name__ == '__main__':
    start_time = time()
#    i = get_raw_html()
#    print 'got %s raw file' % i
    j = digest_oicq_iq()
    print '%s has been digested' % j
    end_time = time()
    print 'Time past: %s\n------ Done ------' % str(end_time - start_time)
