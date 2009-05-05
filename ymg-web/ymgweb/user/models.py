#coding=utf8
from appengine_django.models import BaseModel
from google.appengine.ext import db

class User(BaseModel):
    # 1, required fields
    email = db.EmailProperty(required=True)#使用verbose_name，在form中不显式声明该field，则verbose_name默认为label
    password = db.StringProperty(required=True)
    status = db.IntegerProperty(verbose_name=u'状态', choices=set([1, 2, 3, 0]))#['enabled','pre_enabled','disabled','deleted']
    # 2, not required fields
    nick_name = db.StringProperty(verbose_name=u'名号')
    birthday = db.DateProperty(verbose_name=u'生日')
    gender = db.IntegerProperty(verbose_name=u'性别', default=- 1, choices=set([1, 0, - 1]))#male,female,unset
    career = db.StringProperty(verbose_name=u'职业')
    residence = db.StringProperty(verbose_name=u'现居')
    score = db.IntegerProperty(verbose_name=u'积分', default=0)
    introduction = db.StringProperty(verbose_name=u'自述', multiline=True)
    create_time = db.DateTimeProperty(auto_now_add=True)#在add的时候，form自动排除
    update_time = db.DateTimeProperty(auto_now=True)#在修改的时候，form自动排除
    # 3, methods
    def __repr__(self):
        if self.nick_name:
            return self.nick_name
        (a, b, c) = self.email.partition('@')
        return a


class UserBehavior(BaseModel):
    """非关键行为记录表"""
    owner = db.ReferenceProperty(User)
    login_count = db.IntegerProperty(verbose_name=u'登录次数', default=0)
    last_login_time = db.DateTimeProperty(verbose_name=u'最后登录时间')
    article_count = db.IntegerProperty(verbose_name=u'文章', default=0)

class Favorite(BaseModel):
    owner = db.ReferenceProperty(User)
    subject = db.StringProperty(required=True)
    
    type = db.IntegerProperty(verbose_name=u'', default=0, choices=set([1, 2, 3]))#humor,riddle,iq...
    content = db.StringProperty()
    link = db.StringProperty()#如果不使用tpye的话
    tags = db.StringProperty(verbose_name=u'标签')
    description = db.StringProperty(verbose_name=u'描述')
    
class Message(BaseModel):
    receiver = db.ReferenceProperty(User, collection_name="message_reveiver_set")
    sender = db.ReferenceProperty(User, collection_name="message_sender_set")
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    
    type = db.IntegerProperty(verbose_name=u'', default=0, choices=set([1, 2, 3]))#收件箱 发件箱 收藏箱 垃圾箱...
    read = db.BooleanProperty()
    create_time = db.DateTimeProperty(auto_now=True)
    
    
    