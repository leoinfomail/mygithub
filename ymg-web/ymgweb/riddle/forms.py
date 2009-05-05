#coding=utf8
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.content.forms import status_choice
from ymgweb.content.models import Content

type_choice = (
    (30000, u'谜语'),
    (30100, u'成人谜语'),
    (30200, u'灯谜'),
    (30300, u'儿童谜语'),
    (30400, u'幽默谜语'),
    (30500, u'字谜'),
)

class RiddleForm(djangoforms.ModelForm):
    subject = forms.CharField(label=u'谜题与谜目', help_text=u'谜语的题目和答案范围', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    content = forms.CharField(label=u'谜底', help_text=u'谜语的答案', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    type = forms.ChoiceField(required=True, label=u'类型', choices=type_choice)
    status = forms.ChoiceField(required=True, label=u'状态', choices=status_choice)
    class Meta:
        model = Content
        exclude = ['author', 'content_a', 'property',
        'source_type', 'source_link', 'good_score', 'bad_score', 'view_count', 'favor_score']

    