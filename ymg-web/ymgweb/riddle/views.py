#coding=utf8
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymg.auth import login_required
from ymg.common.webutils import object_list_page
from ymgweb.content.models import Content
from ymgweb.riddle.forms import RiddleForm
from ymgweb.utils import get_cached_promotion_data
from ymgweb.utils import get_pre_next_data
from ymgweb.utils.constants import content_type
from ymgweb.utils.constants import size

@login_required
def add(request):
    if request.method == 'POST':
        form = RiddleForm(request.POST)
        if form.is_valid():
            riddle = form.save(commit=False)
            riddle.author = request.web_user.get_user()
            riddle.put()
            return render_to_response('riddle/add.html',
                {'form':RiddleForm(), 'success_msg':u'成功添加谜语：%s' % riddle.subject})
    else:
        form = RiddleForm()
    return render_to_response('riddle/add.html', {'form':form}, context_instance=RequestContext(request))

def index(request):
    channel_best_riddle = get_cached_promotion_data('channel_best_riddle')
    return render_to_response('riddle/index.html',
        {'channel_best_riddle':channel_best_riddle},
            context_instance=RequestContext(request))

def latest(request, page_id):
    riddle_set = Content.all().filter('type >=', content_type.RIDDLE).filter('type <=', content_type.RIDDLE_MAX).order('type').order('-create_time')
    return object_list_page(request, queryset=riddle_set, per_page=size.DEFAULT_LIST,
        template_name='riddle/latest.html',
        page=page_id, extra_context={'url_prefix':r'/riddle/latest/'})

def view(request, riddle_id):
    if not riddle_id:
        return HttpResponseRedirect('/')
    try:
        id = int(riddle_id)
    except ValueError:
        raise Http404
    riddle = Content.get_by_id(id)
    if not riddle or riddle.type < content_type.RIDDLE or riddle.type > content_type.RIDDLE_MAX:
        raise Http404
    riddle.view_count += 1
    riddle.put()
    #pre next
    (riddle_pre, riddle_next) = get_pre_next_data(id, riddle.type)
    return render_to_response('riddle/view.html', {'riddle':riddle, 'riddle_pre':riddle_pre, 'riddle_next':riddle_next}, context_instance=RequestContext(request))

def riddle(request, template):
    """静态模板呈现"""
    if not template:
        return HttpResponseRedirect('/')
    try:
        return render_to_response('riddle/static/%s.html' % template, context_instance=RequestContext(request))
    except Exception, e:
        raise Http404