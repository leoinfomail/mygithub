#coding=utf8
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.content.models import Content

"""这里用于定义通用的对Content模型的操作表单对象。具体映射到逻辑模型上，在各自模块的forms中定义。"""

source_choice = (
    (0, u'互联网'),
    (1, u'原创'),
)
type_choice = (
    (10000, u'幽默'),
    #
    (20000, u'脑筋急转弯'),
    #
    (30000, u'谜语'),
    (30100, u'成人谜语'),
    (30200, u'灯谜'),
    (30300, u'儿童谜语'),
    (30400, u'幽默谜语'),
    (30500, u'字谜'),
)
status_choice = (
    (1, u'发布'),
    (2, u'暂存'),
    (3, u'关闭'),
    (0, u'删除'),
)

class ContentManageForm(djangoforms.ModelForm):
    """统一的内容管理表单"""
    type = forms.ChoiceField(required=True, label=u'类型', choices=type_choice)
    subject = forms.CharField(label=u'标题', help_text=u'文章的标题', max_length=500, widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    content = forms.CharField(label=u'内容', help_text=u'文章的内容', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    content_a = forms.CharField(required=False, label=u'内容二', help_text=u'内容二', widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
    source_type = forms.ChoiceField(required=False, label=u'来源', choices=source_choice)
    source_link = forms.CharField(required=False, label=u'来源链接', help_text=u'网址链接，会员主页',
        max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
    property = forms.CharField(required=False, label=u'属性', help_text=u'预留属性',
        max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
    status = forms.ChoiceField(required=True, label=u'状态', choices=status_choice)
    good_score = forms.CharField(label=u'好评', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
    bad_score = forms.CharField(label=u'差评', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
    favor_score = forms.CharField(label=u'收藏量', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
    view_count = forms.CharField(label=u'浏览量', help_text=u'', max_length=8, widget=forms.TextInput(attrs={'size':'60'}))
    class Meta:
        model = Content
        exclude = ['author']
