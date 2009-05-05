#coding=utf8
import base64
from django.http import HttpResponseRedirect
import logging

def login_required(func):
    def _wrapper(request, * args, ** kw):
        if not request.web_user.is_anonymous_user():
            return func(request, * args, ** kw)
        else:
            redirect_to = request.path
            return HttpResponseRedirect('/user/login/?redirect_to=%s' % redirect_to)
    return _wrapper

def build_ymg_cookie(email, password):
    '''暂时使用base64编码，伪加密。password已经散列。'''
    plan_text = 'email=' + email + ';' + 'password=' + password;
    cipher_text = base64.b64encode(plan_text)
    return cipher_text
    
def parse_ymg_cookie(cookie):
    if not cookie:
        return {}
    cookie_data = {}
    plan_text = base64.b64decode(cookie)
    for item in plan_text.split(';'):
        _item = item.split('=')
        cookie_data[_item[0]] = _item[1]
    #logging.debug('parse ymg cookie result:')
    #logging.debug(cookie_data)
    return cookie_data