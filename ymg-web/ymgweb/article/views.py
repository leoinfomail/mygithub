#coding=utf8
#import logging
#
#from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import Context, RequestContext, loader
#from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
#
#from google.appengine.api import memcache
#
#from ymg.common.webutils import object_list_page
#from ymg.auth import login_required
#from ymgweb.article.forms import ArticleForm
#from ymgweb.article.models import Article
#
#@login_required
#def add(request):
#    if request.method == 'POST':
#        form = ArticleForm(request.POST)
#        if form.is_valid():
#            article = form.save(commit=False)
#            article.author = request.web_user.get_user()
#            article.put()
#            article.category.article_count += 1
#            article.category.put()
#            return render_to_response('article/add.html',
#                                      {'form':ArticleForm(), 'success_msg':u'成功添加文章：%s' % article.title})
#            return HttpResponseRedirect('/article/add/')
#    else:
#        form = ArticleForm()
#    return render_to_response('article/add.html', {'form':form})
#
#@login_required
#def edit(request, article_id):
#    if not article_id:
#        return HttpResponseRedirect('/')
#    try:
#        id = int(article_id)
#    except ValueError:
#        raise Http404
#    article = Article.get_by_id(id)
#    # check if the article belongs to current user
#    if not article:
#        raise Http404
#    if request.method == 'POST':
#        form = ArticleForm(request.POST)
#        if form.is_valid():
#            edit_article = form.save(commit=False)
#            article.category = edit_article.category
#            article.title = edit_article.title
#            article.content = edit_article.content
#            article.source = edit_article.source
#            article.source_link = edit_article.source_link
#            article.tags = edit_article.tags
#            article.status = edit_article.status
#            article.put()
#            return render_to_response('article/edit.html', {'form':form, 'article_id':article_id, 'success_msg':u'成功修改文章'})
#        return render_to_response('article/edit.html', {'form':form, 'article_id':article_id})
#    form = ArticleForm(instance=article)
#    return render_to_response('article/edit.html', {'form':form, 'article_id':article_id})
#
#def list(request, page_id):
#    article_s = Article.all().order('-create_time')
#    return object_list_page(request, queryset=article_s, per_page=ymgconst.ARTICLE_LIST_PAGE_SIZE,
#                            template_name='article/list.html',
#                            page=page_id, extra_context={'url_prefix':r'/article/list/'})
#
#def view(request, article_id):
#    if not article_id:
#        return HttpResponseRedirect('/')
#    try:
#        id = int(article_id)
#    except ValueError:
#        raise Http404
#    article = Article.get_by_id(id)
#    if not article:
#        raise Http404
#    article.view_count += 1
#    article.put()
#    return render_to_response('article/view.html', {'article':article})