#coding=utf8
import logging
import ymgconst
from ymg.auth import parse_ymg_cookie
from ymgweb.user.models import User

class UserMiddleware(object):
    def process_request(self, request):
        request.web_user = WebUser(request)
        return None

class AnonymousUser():
    pass

class WebUser():
    '''fixme'''
    def __init__(self, request=None):
        self.request = request
        self.web_user = None #内含的web_user用来记录真正login的用户信息。外部的WebUser本身用来判断状态，作工具类。
        
    def is_anonymous_user(self):
        # if not initialized
        if not self.web_user:
            #logging.debug('web_user is none')
            self.get_web_user()
        if isinstance(self.web_user, AnonymousUser):
            #logging.debug('is anonymous')
            return True
        return False
    
    def get_web_user(self):
        '''从cookie中的数据建立WebUser对象，注意返回的是内含的web_user'''
        if self.web_user:
            #logging.debug('cached web_user returned')
            return self.web_user
        ymg_cookie = self.request.COOKIES.get(ymgconst.YMG_COOKIE, None)
        if not ymg_cookie:
            #logging.debug('no cookie, anonymous returned')
            self.web_user = AnonymousUser()
            return self.web_user
        cookie_data = parse_ymg_cookie(ymg_cookie)
        self.web_user = WebUser()
        self.web_user.email = cookie_data.get('email', None)
        self.web_user.password = cookie_data.get('password', None)
        return self.web_user
    
    def get_user(self):
        '''取得User，注意，不是WebUser'''
        if self.is_anonymous_user():
            return None
        if self.web_user.email:
            user = User.all().filter('email', self.web_user.email)
            if user.count() == 1:
                return user[0]
        return None
        