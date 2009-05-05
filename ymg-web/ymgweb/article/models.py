#coding=utf8
#from appengine_django.models import BaseModel
#from google.appengine.ext import db
#
#from ymgweb.user.models import User
#from ymgweb.category.models import Category
#
#class Article(BaseModel):
#    category = db.ReferenceProperty(Category, verbose_name=u'类别', required=True)
#    title = db.StringProperty(required=True)
#    content = db.TextProperty(required=True)
#    author = db.ReferenceProperty(User)
#
#    source = db.IntegerProperty(verbose_name=u'来源',default=0,choices=set([0,1]))#['互联网','原创']
#    source_link = db.StringProperty(verbose_name=u'来源链接')# 网址链接，会员主页
#    tags = db.StringProperty(verbose_name=u'标签')
#    view_count = db.IntegerProperty(default=0)
#    good_score = db.IntegerProperty(default=0)
#    bad_score = db.IntegerProperty(default=0)
#    status = db.IntegerProperty(verbose_name=u'状态',choices=set([1,2,3,0]))#['published','edit','closed','deleted']
#    create_time = db.DateTimeProperty(auto_now_add=True)#在add的时候，form自动排除
#    update_time = db.DateTimeProperty(auto_now=True)#在修改的时候，form自动排除
