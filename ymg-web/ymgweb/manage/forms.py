#coding=utf8
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.manage.models import Promotion

"""
home_best_humor
home_best_riddle
home_best_iq

home_quote_humor
home_quote_iq
home_quote_riddle

channel_best_humor
channel_best_iq
channel_best_riddle

detail_acd_humor
detail_acd_iq
detail_acd_riddle

"""

class PromotionForm(djangoforms.ModelForm):
    subject = forms.CharField(label=u'推荐项目', help_text=u'命名规则：页面模块名_内容名_模型(home_best_humor)', widget=forms.TextInput(attrs={'size':'30'}))
    content = forms.CharField(label=u'内容', help_text=u'使用内容的id并用,分隔', widget=forms.TextInput(attrs={'size':'80'}))
    description = forms.CharField(required=False, label=u'描述', help_text=u'', widget=forms.TextInput(attrs={'size':'80'}))
    class Meta:
        model = Promotion

class PromotionEditForm(djangoforms.ModelForm):
    subject = forms.CharField(label=u'推荐项目', help_text=u'命名规则：一级_二级_模型(home_best_humor)', widget=forms.TextInput(attrs={'size':'30', 'readonly':'true'}))
    content = forms.CharField(label=u'内容', help_text=u'使用内容的id并用,分隔', widget=forms.TextInput(attrs={'size':'80'}))
    description = forms.CharField(required=False, label=u'描述', help_text=u'', widget=forms.TextInput(attrs={'size':'80'}))
    class Meta:
        model = Promotion