#coding=utf8

def request(request):
    return {'request': request}

def web_user(request):
    """as ymg.auth.middleware.UserMiddleware, there must be a web_user"""
    ctx = {'web_user':request.web_user}
    return ctx