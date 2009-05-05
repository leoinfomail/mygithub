#coding=utf8
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.content.forms import status_choice
from ymgweb.content.models import Content

type_choice = (
    (10000, u'幽默'),
)

class HumorForm(djangoforms.ModelForm):
    subject = forms.CharField(label=u'标题', help_text=u'文章的标题', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    content = forms.CharField(label=u'内容', help_text=u'文章的内容', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    type = forms.ChoiceField(required=True, label=u'类型', choices=type_choice)
    status = forms.ChoiceField(required=True, label=u'状态', choices=status_choice)
    class Meta:
        model = Content
        exclude = ['author', 'content_a', 'property',
        'source_type', 'source_link', 'good_score', 'bad_score', 'view_count', 'favor_score']

#class HumorForm(djangoforms.ModelForm):
#    title = forms.CharField(label=u'标题', help_text=u'文章的标题', max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
#    content = forms.CharField(min_length=5, label=u'内容', help_text=u'文章的内容',
#        widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
#    tags = forms.MultipleChoiceField(required=False, label=u'标签', help_text=u'可以多选',
#        choices=tag_choice, widget=forms.CheckboxSelectMultiple())
#    source_type = forms.ChoiceField(required=False, label=u'来源', choices=source_choice)
#    source_link = forms.CharField(required=False, label=u'来源链接', help_text=u'网址链接，会员主页',
#        max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
#    status = forms.ChoiceField(required=False, label=u'状态', choices=status_choice)
#    class Meta:
#        model = Humor
#        exclude = ['author', 'good_score', 'bad_score', 'view_count', 'favor_score']
#
#class HumorFormManage(djangoforms.ModelForm):
#    title = forms.CharField(label=u'标题', help_text=u'文章的标题', max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
#    content = forms.CharField(min_length=5, label=u'内容', help_text=u'文章的内容',
#        widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
#    tags = forms.MultipleChoiceField(required=False, label=u'标签', help_text=u'可以多选',
#        choices=tag_choice, widget=forms.CheckboxSelectMultiple())
#    source_type = forms.ChoiceField(required=False, label=u'来源', choices=source_choice)
#    source_link = forms.CharField(required=False, label=u'来源链接', help_text=u'网址链接，会员主页',
#        max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
#    status = forms.ChoiceField(required=False, label=u'状态', choices=status_choice)
#    good_score = forms.CharField(label=u'好评', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
#    bad_score = forms.CharField(label=u'差评', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
#    favor_score = forms.CharField(label=u'收藏量', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
#    view_count = forms.CharField(label=u'浏览量', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
#    class Meta:
#        model = Humor
#        exclude = ['author']
