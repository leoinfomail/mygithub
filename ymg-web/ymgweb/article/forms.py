#coding=utf8
#from django import newforms as forms
#from google.appengine.ext.db import djangoforms
#from ymgweb.article.models import Article
#from ymgweb.category.models import Category

#class CategoryForm(djangoforms.ModelForm):
#    name = forms.CharField(label=u'分类', help_text=u'分类的名称')
#    class Meta:
#        model = Category
#        exclude = ['article_count']
#
#source_choice = (
#    (0, u'互联网'),
#    (1, u'原创'),
#)
#tag_choice = (
#    (u'搞笑', u'搞笑'),
#    (u'幽默', u'幽默'),
#)
#status_choice = (
#    (1, u'发布'),
#    (2, u'暂存'),
#    (3, u'关闭'),
#    (0, u'删除'),
#)
#class ArticleForm(djangoforms.ModelForm):
#    title = forms.CharField(label=u'标题', help_text=u'文章的标题', max_length=500,
#        widget=forms.TextInput(attrs={'size':'60'}))
#    content = forms.CharField(min_length=2, label=u'内容', help_text=u'文章的内容',
#        widget=forms.Textarea(attrs={'class':'special', 'rows':'10', 'cols':'50'}))
#    tags = forms.MultipleChoiceField(required=False, label=u'标签', help_text=u'可以多选',
#        choices=tag_choice, widget=forms.CheckboxSelectMultiple())
#    source = forms.ChoiceField(required=False, label=u'来源', choices=source_choice)
#    source_link = forms.CharField(required=False, label=u'来源链接', help_text=u'网址链接，会员主页', max_length=500, widget=forms.TextInput(attrs={'size':'60'}))
#    status = forms.ChoiceField(required=False, label=u'状态', choices=status_choice)
#    #content = forms.Textarea() 直接使用Textarea的话，不能指定了其他属性了
#    #update_time = forms.DateTimeField(widget=forms.DateTimeField)???
#    class Meta:
#        model = Article
#        exclude = ['author', 'good_score', 'bad_score', 'view_count']
#
#class ArticleEditForm(djangoforms.ModelForm):
#    '''没有使用'''
#    class Meta:
#        model = Article
#        exclude = []
    