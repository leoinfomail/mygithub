#coding=utf8
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymg.auth import login_required
from ymg.common.webutils import object_list_page
from ymgweb.content.forms import ContentManageForm
from ymgweb.content.models import Content
from ymgweb.manage.forms import PromotionEditForm
from ymgweb.manage.forms import PromotionForm
from ymgweb.manage.models import Promotion
from ymgweb.utils.constants import content_type
from ymgweb.utils.constants import size


#只为数据订正
@login_required
def change(request):
#    data_list = Content.all()
#    for data in data_list:
#        data.type = 10000
#        data.put()
    return HttpResponseRedirect('/')

def style_center(request):
    return render_to_response('manage/style_center.html')

@login_required
def url_list(request):
    return render_to_response('manage/url_list.html', context_instance=RequestContext(request))

@login_required
def index(request):
    return render_to_response('manage/manage.html', {}, context_instance=RequestContext(request))

@login_required
def content_edit(request, content_id):
    if not content_id:
        return HttpResponseRedirect('/')
    try:
        id = int(content_id)
    except ValueError:
        raise Http404
    data = Content.get_by_id(id)
    if not data:
        raise Http404
    if request.method == 'POST':
        form = ContentManageForm(request.POST)
        if form.is_valid():
            edit_data = form.save(commit=False)
            data.subject = edit_data.subject
            data.content = edit_data.content
            data.content_a = edit_data.content_a
            data.source_type = edit_data.source_type
            data.source_link = edit_data.source_link
            data.property = edit_data.property
            data.type = edit_data.type
            data.status = edit_data.status
            data.good_score = edit_data.good_score
            data.bad_score = edit_data.bad_score
            data.favor_score = edit_data.favor_score
            data.view_count = edit_data.view_count
            data.put()
            return render_to_response('manage/content_edit.html', {'form':form, 'content_id':content_id, 'success_msg':u'成功修改'},
                context_instance=RequestContext(request))
        return render_to_response('manage/content_edit.html', {'form':form, 'content_id':content_id}, context_instance=RequestContext(request))
    form = ContentManageForm(instance=data)
    return render_to_response('manage/content_edit.html', {'form':form, 'content_id':content_id}, context_instance=RequestContext(request))

def delete_content_by_id(id):
    """统一的删除内容工具函数，没有加类型校验"""
    data = Content.get_by_id(id)
    if data:
        data.delete()
    else:
        raise Http404

# humor start
@login_required
def humor_data(request, page_id):
    humor_set = Content.all().filter('type >=', content_type.HUMOR).filter('type <=', content_type.HUMOR_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=humor_set, per_page=size.DEFAULT_MANAGE_LIST,
        template_name='manage/content_list.html',
        page=page_id, extra_context={'url_prefix':r'/manage/humor_data/', 'type':'humor'})

@login_required
def humor_delete(request, humor_id):
    if not humor_id:
        return HttpResponseRedirect('/')
    try:
        id = int(humor_id)
    except ValueError:
        raise Http404
    delete_content_by_id(id)
    return HttpResponseRedirect('/manage/humor_data/')
# humor end


#@login_required
#def humor_edit(request, humor_id):
#    if not humor_id:
#        return HttpResponseRedirect('/')
#    try:
#        id = int(humor_id)
#    except ValueError:
#        raise Http404
#    humor = Content.get_by_id(id)
#    if not humor or humor.type != 1:
#        raise Http404
#    if request.method == 'POST':
#        form = HumorManageForm(request.POST)
#        if form.is_valid():
#            edit_humor = form.save(commit=False)
#            humor.subject = edit_humor.subject
#            humor.content = edit_humor.content
#            humor.source_type = edit_humor.source_type
#            humor.source_link = edit_humor.source_link
#            humor.property = edit_humor.property
#            humor.status = edit_humor.status
#            humor.good_score = edit_humor.good_score
#            humor.bad_score = edit_humor.bad_score
#            humor.favor_score = edit_humor.favor_score
#            humor.view_count = edit_humor.view_count
#            humor.put()
#            return render_to_response('manage/humor_edit.html', {'form':form, 'humor_id':humor_id, 'success_msg':u'成功修改'},
#                context_instance=RequestContext(request))
#        return render_to_response('manage/humor_edit.html', {'form':form, 'humor_id':humor_id}, context_instance=RequestContext(request))
#    form = HumorManageForm(instance=humor)
#    return render_to_response('manage/humor_edit.html', {'form':form, 'humor_id':humor_id}, context_instance=RequestContext(request))

# iq start
@login_required
def iq_data(request, page_id):
    iq_set = Content.all().filter('type >=', content_type.IQ).filter('type <=', content_type.IQ_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=iq_set, per_page=size.DEFAULT_MANAGE_LIST,
        template_name='manage/content_list.html',
        page=page_id, extra_context={'url_prefix':r'/manage/iq_data/', 'type':'iq'})

@login_required
def iq_delete(request, iq_id):
    if not iq_id:
        return HttpResponseRedirect('/')
    try:
        id = int(iq_id)
    except ValueError:
        raise Http404
    delete_content_by_id(id)
    return HttpResponseRedirect('/manage/iq_data/')
# iq end

# riddle start
@login_required
def riddle_data(request, page_id):
    riddle_set = Content.all().filter('type >=', content_type.RIDDLE).filter('type <=', content_type.RIDDLE_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=riddle_set, per_page=size.DEFAULT_MANAGE_LIST,
        template_name='manage/content_list.html',
        page=page_id, extra_context={'url_prefix':r'/manage/riddle_data/', 'type':'riddle'})

@login_required
def riddle_delete(request, riddle_id):
    if not riddle_id:
        return HttpResponseRedirect('/')
    try:
        id = int(riddle_id)
    except ValueError:
        raise Http404
    delete_content_by_id(id)
    return HttpResponseRedirect('/manage/riddle_data/')
# riddle end

# promotion start
@login_required
def promotion(request):
    promotion_set = Promotion.all().order('subject')
    return render_to_response('manage/promotion.html', {'promotion_set':promotion_set}, context_instance=RequestContext(request))

@login_required
def add_promotion(request):
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            check_data = Promotion.all().filter('subject =', promotion.subject).get()
            if check_data:
                return render_to_response('manage/add_promotion.html', {'form':form, 'error_msg':u'重复添加：%s' % promotion.subject}, context_instance=RequestContext(request))
            promotion.put()
            return render_to_response('manage/add_promotion.html', {'form':form, 'success_msg':u'成功添加：%s' % promotion.subject}, context_instance=RequestContext(request))
    else:
        form = PromotionForm()
    return render_to_response('manage/add_promotion.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit_promotion(request, promotion_id):
    if not promotion_id:
        return HttpResponseRedirect('/')
    try:
        promotion_id = int(promotion_id)
    except ValueError:
        raise Http404
    promotion = Promotion.get_by_id(promotion_id)
    if not promotion:
        raise Http404
    if request.method == 'POST':
        form = PromotionEditForm(request.POST)
        if form.is_valid():
            edit_promotion = form.save(commit=False)
            promotion.subject = edit_promotion.subject
            promotion.content = edit_promotion.content
            promotion.description = edit_promotion.description
            promotion.put()
            #return render_to_response('manage/edit_promotion.html', {'form':form, 'promotion_id':promotion_id, 'success_msg':u'成功修改'}, context_instance=RequestContext(request))
            return HttpResponseRedirect('/manage/promotion/')
    else:
        form = PromotionEditForm(instance=promotion)
    return render_to_response('manage/edit_promotion.html', {'form':form, 'promotion_id':promotion_id}, context_instance=RequestContext(request))

@login_required
def delete_promotion(request, promotion_id):
    if not promotion_id:
        return HttpResponseRedirect('/')
    try:
        promotion_id = int(promotion_id)
    except ValueError:
        raise Http404
    promotion = Promotion.get_by_id(promotion_id)
    if not promotion:
        raise Http404
    promotion.delete()
    return HttpResponseRedirect('/manage/promotion/')