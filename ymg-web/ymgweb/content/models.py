#coding=utf8
from appengine_django.models import BaseModel
from google.appengine.ext import db
from ymgweb.user.models import User

"""
目前尚未支持图片，gae上怎么搞？
"""

class Content(BaseModel):
    """所有内容的模型类"""
    subject = db.TextProperty(required=True)
    content = db.TextProperty(required=True)
    author = db.ReferenceProperty(User)
    type = db.IntegerProperty(required=True) #10000:humor,20000:iq,30000:riddle
    status = db.IntegerProperty(verbose_name=u'状态', default=1, choices=set([1, 2, 3, 0]))#['published','edit','closed','deleted'] 生命周期的表示

    content_a = db.TextProperty()
    source_type = db.IntegerProperty(verbose_name=u'来源', default=0, choices=set([0, 1]))#['互联网','原创']
    source_link = db.StringProperty(verbose_name=u'来源链接')# 网址链接，会员主页
    property = db.StringProperty(verbose_name=u'属性')
    view_count = db.IntegerProperty(default=0)
    good_score = db.IntegerProperty(default=0)
    bad_score = db.IntegerProperty(default=0)
    favor_score = db.IntegerProperty(default=0) #收藏数
    create_time = db.DateTimeProperty(auto_now_add=True) #在add的时候，form自动排除
    update_time = db.DateTimeProperty(auto_now=True) #在修改的时候，form自动排除

