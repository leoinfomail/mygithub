#coding=utf8
# ---------------------------
# 注意这里的forms和标准的django有一定区别
# django里面只有django.forms。gae里面使用老的。所以暂时使用newforms as forms
# 1.0中使用error_message
# ---------------------------
from django import newforms as forms
from google.appengine.ext.db import djangoforms
from ymgweb.user.models import User

gender_choice = (
    (1, u'男'),
    (0, u'女'),
    (-1, u'未设定'),
)

class UserRegForm(djangoforms.ModelForm):
    email = forms.EmailField(label=u'你的邮件', help_text=u'用于登录、取回密码等', max_length=64)
    password = forms.CharField(label=u'登录密码', help_text=u'最长26位的密码', max_length=26, widget=forms.PasswordInput())
    class Meta:
        model = User
        exclude = ['nick_name', 'birthday', 'gender', 'residence', 'score',
            'career', 'introduction', 'status']

class UserEditForm(djangoforms.ModelForm):
    email = forms.EmailField(label=u'你的邮件', help_text=u'用于登录、取回密码等', max_length=64, widget=forms.TextInput(attrs={'readonly':'true'}))
    password = forms.CharField(label=u'密码', help_text=u'最长26位的密码，如不需要修改，请保持不变', max_length=26, widget=forms.PasswordInput())
    #password_2 = forms.CharField(label=u'确认密码',help_text=u'最长26位的密码',max_length=26,widget=forms.PasswordInput())
    #birthday = forms.DateField(required=False,label=u'生日')如何融入一个日期时间选择器?
    gender = forms.ChoiceField(required=False, label=u'性别', choices=gender_choice)
    introduction = forms.CharField(required=False, label=u'自述', help_text=u'最长500字符', max_length=500, widget=forms.Textarea())
    class Meta:
        model = User
        exclude = ['score', 'status']

class UserLoginForm(djangoforms.ModelForm):
    email = forms.EmailField(label=u'邮件', help_text=u'', max_length=64)
    password = forms.CharField(label=u'密码', help_text=u'', max_length=26, widget=forms.PasswordInput(attrs={'size':'20'}))
    class Meta:
        model = User
        exclude = ['nick_name', 'birthday', 'gender', 'residence', 'score',
            'career', 'introduction', 'status']

