#coding=utf8
import urllib2
import logging

class LoggingRedirectHandler(urllib2.HTTPRedirectHandler):
    logger = logging.getLogger('httpError')
    def http_error_301(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        self.__class__.logger.info('[' + str(code) + ']: ' + req.get_full_url())
        result.code = code
        return result

    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
        self.__class__.logger.info('[' + str(code) + ']: ' + req.get_full_url())
        result.code = code
        return result

class DefaultErrorHandler(urllib2.HTTPDefaultErrorHandler):
    logger = logging.getLogger('httpError')
    def http_error_default(self, req, fp, code, msg, headers):
        """返回404页面内容，设置code"""
        result = urllib2.HTTPError(req.get_full_url(), code, msg, headers, fp)
        self.__class__.logger.info('[' + str(code) + ']: ' + req.get_full_url())
        result.code = code
        return result
