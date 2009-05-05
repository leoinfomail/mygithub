#coding=utf8
import cookielib
import urllib
import urllib2
from time import time

from com.youmogan.poster.engine import PostEngine
from com.youmogan.poster.loader import IqDataLoader
from com.youmogan.poster.loader import RiddleDataLoader
from com.youmogan.spider.http_handler import DefaultErrorHandler
from com.youmogan.spider.http_handler import LoggingRedirectHandler
from com.youmogan.spider.url_generater import out_text_dir
from com.youmogan.spider.url_generater import out_text_dir_

__author__ = "jun.yanj"
__date__ = "$2008-11-23 22:19:49$"

def local_post_test():
    """本地研究"""
    login_url = r'http://localhost:8080/user/login/'
    login_data = urllib.urlencode([
    ('email', 'leoyoung@126.com'),
    ('password', 'hello1'), ])
    cj = cookielib.CookieJar()
    logined_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), LoggingRedirectHandler(), DefaultErrorHandler)
    #login_request = urllib2.Request(login_url)
    #这里将logined_opener安装到urllib2上，之后的open操作可以不使用
    #logined_opener.open(login_request, login_data)或者
    #logined_opener.open(login_url, login_data)
    #而是使用urllib2.urlopen(login_request, login_data)或者也可以不创建request对象，直接使用
    #urllib2.urlopen(login_url, login_data)
    urllib2.install_opener(logined_opener)
    login_response = urllib2.urlopen(login_url, login_data)
    data_url = r'http://localhost:8080/humor/add/'
    data = urllib.urlencode([
    ('title', '<p>ssssss八</p>'),
    ('content', '<p>aaaaaa5<p>')])
    resource = urllib2.urlopen(data_url, data)
    print resource.read()

def local_post():
    """本地gae开发用"""
    login_url = r'http://localhost:8080/user/login/'
    login_data = urllib.urlencode([('email', 'leoyoung@126.com'), ('password', 'hello1')])
    poster_engine = PostEngine(login_url=login_url, login_data=login_data)
    #humor
#    post_url = r'http://localhost:8080/humor/add/'
#    loader = HumorDataLoader(_out_text_dir_)
#    post_url = r'http://localhost:8080/riddle/add/'
#    loader = RiddleDataLoader(out_text_dir)
    post_url = r'http://localhost:8080/iq/add/'
    loader = IqDataLoader(out_text_dir_)
    poster_engine.load_post_data(loader)
    count = poster_engine.post(post_url)
    print '%s done' % count

def ymg_post():
    """线上发布"""
    login_url = r'http://www.youmogan.com/user/login/'
    login_data = urllib.urlencode([('email', 'xiaoshijie@gmail.com'), ('password', 'exceptional')])
    poster_engine = PostEngine(login_url=login_url, login_data=login_data)
    #humor
#    loader = HumorDataLoader(out_text_dir)
    post_url = r'http://www.youmogan.com/iq/add/'
    loader = IqDataLoader(out_text_dir_)
    poster_engine.load_post_data(loader)
    count = poster_engine.post(post_url)
    print '%s posted' % count

if __name__ == "__main__":
    start_time = time()
    ymg_post()
#    local_post()
    end_time = time()
    print 'Time past: %s\n------ Done ------' % str(end_time - start_time)



