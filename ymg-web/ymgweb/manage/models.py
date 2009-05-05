#coding=utf8
from appengine_django.models import BaseModel
from google.appengine.ext import db

class Promotion(BaseModel):
    subject = db.StringProperty(required=True)
    content = db.StringProperty()#逗号分隔
    description = db.StringProperty()
