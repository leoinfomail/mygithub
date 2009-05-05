#coding=utf8
import StringIO
import gzip
import logging
import urllib2

from com.youmogan.spider.http_handler import DefaultErrorHandler
from com.youmogan.spider.http_handler import LoggingRedirectHandler

"""
这个实际上是一个静态工具类，python中怎么表示比较好？
logger根据错误级别不同的输出怎么做，现在只有非别取两个不同设置的logger
"""
class HtmlSourceGetter(object):
    """
    取得HTML源码的工具类。统一转换编码为uft8
    """
    logger = logging.getLogger('httpRequest')
    user_agent = {'Firefox':r'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1',
        'Chrome':r'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
        'IE':r'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; CIBA)'}
    def get_uniform_html_source(self, url, coding=None):
        """
        得到给定url的html源码，以dict形式返回。
        如果知道编码，可以指定编码，（不指定则会自动检测编码，除非头里面得不到）。
        最后统一转换成utf-8。
        请求返回失败的话，返回data为None的字典
        """
        if not url:
            raise ValueError, 'url should not be empty'
        the_request = urllib2.Request(url)
        # add headers
        the_request.add_header('User-Agent', self.user_agent['Firefox'])
        the_request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener(LoggingRedirectHandler(), DefaultErrorHandler())       
        resource = opener.open(the_request)
        if not hasattr(resource, 'code'):
            resource.code = 200
        self.logger.info('[' + str(resource.code) + ']: ' + url) #repr(resource.headers.items())
        result = {'request_url':url, 'host':the_request.get_host(), 'data':None}
        if resource.code in range(200, 400, 1):
            result['data'] = resource.read()
            if resource.headers.get('content-encoding', '') == 'gzip':
                result['data'] = self.un_gzip(result['data'])
            if not coding:
                coding = self.get_coding(resource.headers)
                if not coding: self.logger.debug('can not get coding!')
            if coding and coding != 'utf-8':
                result['data'] = self.converter_coding(result['data'], coding)
            if result['data'] is None:
                logging.getLogger('httpError').error('converter_coding failed: ' + result['request_url'])
        return result
        
    def get_coding(self, headers):
        """得到小写的编码，得不到返回None"""
        content_types = [elem.strip() for elem in headers.get('content-type', '').split(';')]
        for elem in content_types:
            (charset_key, equal_sign, charset) = elem.partition('=')
            if charset_key == 'charset':
                return charset.lower()
        return None
    
    def converter_coding(self, data, from_coding, to_coding='utf-8'):
        """转换编码，失败返回None"""
        try:
            return data.decode(from_coding).encode(to_coding)
        except UnicodeDecodeError:
            return None
        
    def un_gzip(self, data):
        return gzip.GzipFile(fileobj=StringIO.StringIO(data)).read()
    