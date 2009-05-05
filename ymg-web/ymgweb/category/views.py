#coding=utf8
#import logging
#
#from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import Context, RequestContext, loader
#from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
#
#from google.appengine.api import memcache
#
#from ymg.auth import login_required
#from ymgweb.category.forms import CategoryForm
#from ymgweb.category.models import Category
#import settings
#
#@login_required
#def add(request):
#    if request.method == 'POST':
#        form = CategoryForm(request.POST)
#        if form.is_valid():
#            category = form.save(commit=False)
#            exist_category = Category.all().filter('name', category.name)
#            if exist_category.count():
#                return render_to_response('category/add.html',
#                                          {'form':form, 'error_msg':u'该类目已经存在'})
#            category.put()
#            return render_to_response('category/add.html',
#                                      {'form':CategoryForm(),'success_msg':u'成功添加类目：%s' % category.name})
#    else:
#        form = CategoryForm()
#    return render_to_response('category/add.html', {'form':form})
