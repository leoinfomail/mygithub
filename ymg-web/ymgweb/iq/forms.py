#coding=utf8
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.content.forms import status_choice
from ymgweb.content.models import Content

type_choice = (
    (20000, u'脑筋急转弯'),
)

class IqForm(djangoforms.ModelForm):
    subject = forms.CharField(label=u'题目', help_text=u'题目', max_length=500, widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    content = forms.CharField(min_length=5, label=u'答案', help_text=u'答案', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    type = forms.ChoiceField(required=True, label=u'类型', choices=type_choice)
    status = forms.ChoiceField(required=True, label=u'状态', choices=status_choice)
    class Meta:
        model = Content
        exclude = ['author', 'content_a', 'property',
        'source_type', 'source_link', 'good_score', 'bad_score', 'view_count', 'favor_score']

    