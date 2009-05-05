#coding=utf8
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymg.auth import login_required
from ymg.common.webutils import object_list_page
from ymgweb.content.models import Content
from ymgweb.iq.forms import IqForm
from ymgweb.utils import get_cached_promotion_data
from ymgweb.utils import get_pre_next_data
from ymgweb.utils.constants import content_type
from ymgweb.utils.constants import size

@login_required
def add(request):
    if request.method == 'POST':
        form = IqForm(request.POST)
        if form.is_valid():
            iq = form.save(commit=False)
            iq.author = request.web_user.get_user()
            iq.put()
            return render_to_response('iq/add.html',
                {'form':IqForm(), 'success_msg':u'成功添加文章：%s' % iq.subject})
            return HttpResponseRedirect('/iq/add/')
    else:
        form = IqForm()
    return render_to_response('iq/add.html', {'form':form}, context_instance=RequestContext(request))

def index(request):
    channel_best_iq = get_cached_promotion_data('channel_best_iq')
    return render_to_response('iq/index.html',
        {'channel_best_iq':channel_best_iq},
            context_instance=RequestContext(request))

def latest(request, page_id):
    iq_set = Content.all().filter('type >=', content_type.IQ).filter('type <=', content_type.IQ_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=iq_set, per_page=size.DEFAULT_LIST,
        template_name='iq/latest.html',
        page=page_id, extra_context={'url_prefix':r'/iq/latest/'})

def view(request, iq_id):
    if not iq_id:
        return HttpResponseRedirect('/')
    try:
        id = int(iq_id)
    except ValueError:
        raise Http404
    iq = Content.get_by_id(id)
    if not iq or iq.type < content_type.IQ or iq.type > content_type.IQ_MAX:
        raise Http404
    iq.view_count += 1
    iq.put()
    #pre next
    (iq_pre, iq_next) = get_pre_next_data(id, iq.type)
    return render_to_response('iq/view.html', {'iq':iq, 'iq_pre':iq_pre, 'iq_next':iq_next}, context_instance=RequestContext(request))

def iq(request, template):
    """静态模板呈现"""
    if not template:
        return HttpResponseRedirect('/')
    try:
        return render_to_response('iq/static/%s.html' % template, context_instance=RequestContext(request))
    except Exception, e:
        raise Http404