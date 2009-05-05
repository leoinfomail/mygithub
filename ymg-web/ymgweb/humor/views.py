#coding=utf8
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymg.auth import login_required
from ymg.common.webutils import object_list_page
from ymgweb.content.models import Content
from ymgweb.humor.forms import HumorForm
from ymgweb.utils import get_cached_promotion_data
from ymgweb.utils import get_pre_next_data
from ymgweb.utils.constants import content_type
from ymgweb.utils.constants import size

@login_required
def add(request):
    """TODO做一个通用的检查器，检查所有进入的文章，不出现br，只用p。便于手工添加文章时，不需要烦人的修改br"""
    if request.method == 'POST':
        form = HumorForm(request.POST)
        if form.is_valid():
            humor = form.save(commit=False)
            humor.author = request.web_user.get_user()
            humor.put()
            return render_to_response('humor/add.html',
                {'form':HumorForm(), 'success_msg':u'成功添加文章：%s' % humor.subject},
                context_instance=RequestContext(request))
    else:
        form = HumorForm()
    return render_to_response('humor/add.html', {'form':form}, context_instance=RequestContext(request))

#@login_required
#def edit(request, humor_id):
#    if not humor_id:
#        return HttpResponseRedirect('/')
#    try:
#        id = int(humor_id)
#    except ValueError:
#        raise Http404
#    humor = Content.get_by_id(id)
#    if not humor or humor.type != 1:
#        raise Http404
#    # TODO check if the humor belongs to current user
#    if request.method == 'POST':
#        form = HumorForm(request.POST)
#        if form.is_valid():
#            edit_humor = form.save(commit=False)
#            humor.subject = edit_humor.subject
#            humor.content = edit_humor.content
#            humor.status = edit_humor.status
#            humor.put()
#            return render_to_response('humor/edit.html', {'form':form, 'humor_id':humor_id, 'success_msg':u'成功修改文章'},
#                context_instance=RequestContext(request))
#        return render_to_response('humor/edit.html', {'form':form, 'humor_id':humor_id}, context_instance=RequestContext(request))
#    form = HumorForm(instance=humor)
#    return render_to_response('humor/edit.html', {'form':form, 'humor_id':humor_id}, context_instance=RequestContext(request))

def index(request):
    channel_best_humor = get_cached_promotion_data('channel_best_humor')
    return render_to_response('humor/index.html',
        {'channel_best_humor':channel_best_humor},
            context_instance=RequestContext(request))

def latest(request, page_id):
    humor_set = Content.all().filter('type >=', content_type.HUMOR).filter('type <=', content_type.HUMOR_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=humor_set, per_page=size.DEFAULT_LIST,
        template_name='humor/latest.html',
        page=page_id, extra_context={'url_prefix':r'/humor/latest/'})
        
def view(request, humor_id):
    if not humor_id:
        return HttpResponseRedirect('/')
    try:
        id = int(humor_id)
    except ValueError:
        raise Http404
    humor = Content.get_by_id(id)
    if not humor or humor.type < content_type.HUMOR or humor.type > content_type.HUMOR_MAX:
        raise Http404
    humor.view_count += 1
    humor.put()
    #pre next
    (humor_pre, humor_next) = get_pre_next_data(id, humor.type)
    return render_to_response('humor/view.html', {'humor':humor, 'humor_pre':humor_pre, 'humor_next':humor_next}, context_instance=RequestContext(request))