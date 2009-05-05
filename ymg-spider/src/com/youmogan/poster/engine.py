#coding=utf8
import cookielib
import urllib
import urllib2

from com.youmogan.spider.http_handler import DefaultErrorHandler
from com.youmogan.spider.http_handler import LoggingRedirectHandler
__author__ = "jun.yanj"
__date__ = "$2008-12-28 20:12:42$"

class PostEngine(object):
    """
    可重用的发布引擎。
    在创建引擎之后，使用不同data_loader和不同的post_url可以重用引擎。
    """
    cj = cookielib.CookieJar()
    logined_opener = None
    def __init__(self, login_url=None, login_data=None, post_url=None):
        self.post_data = []
        self.post_url = post_url
        if login_url is not None and login_data is not None:
            self.__class__.logined_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.__class__.cj), LoggingRedirectHandler(), DefaultErrorHandler)
            urllib2.install_opener(self.__class__.logined_opener)
            urllib2.urlopen(login_url, login_data)

    def load_post_data(self, data_loader):
        """使用特定的loader将本地数据加载到post_data中。返回加载的数目"""
        self.post_data = data_loader.parse_data()
        return len(self.post_data)

    def post(self, post_url=None):
        """将post_data中的数据urlencode后post，返回完成数目"""
        if post_url:
            self.post_url = post_url
        elif not self.post_url:
            raise ValueError, 'ymg: post_url is None'
        if not self.post_data:
            raise ValueError, 'ymg: post_data is empty'
        count = 0
        for data in self.post_data:
            urllib2.urlopen(self.post_url, urllib.urlencode(data))
            print 'done: ' + str(count)
            count += 1
        return count
    
if __name__ == "__main__":
    print "Hello";