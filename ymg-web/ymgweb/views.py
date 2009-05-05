#coding=utf8
import logging

from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymgweb.content.models import Content
from ymgweb.user.forms import UserLoginForm
from ymgweb.utils import get_cached_promotion_data
from ymgweb.utils import get_one_cached_promotion_data

def home(request):
    #tab
    home_best_humor = get_cached_promotion_data('home_best_humor')
    home_best_iq = get_cached_promotion_data('home_best_iq')
    home_best_riddle = get_cached_promotion_data('home_best_riddle')
    #quote
    home_quote_humor = get_one_cached_promotion_data('home_quote_humor')
    home_quote_iq = get_one_cached_promotion_data('home_quote_iq')
    home_quote_riddle = get_one_cached_promotion_data('home_quote_riddle')
    #login
    if request.web_user.is_anonymous_user():
        login_form = UserLoginForm()
    else:
        login_form = None
    return render_to_response('home.html',
        {'home_best_humor':home_best_humor,
            'home_best_iq':home_best_iq,
            'home_best_riddle':home_best_riddle,
            'home_quote_humor':home_quote_humor,
            'home_quote_iq':home_quote_iq,
            'home_quote_riddle':home_quote_riddle,
            'login_form':login_form},
            context_instance=RequestContext(request))

# ajax
def home_best_humor(request):
    #sleep(0.5)
    home_best_humor = get_cached_promotion_data('home_best_humor')
    return render_to_response('home/home_best_humor.html',
        {'home_best_humor':home_best_humor},
        context_instance=RequestContext(request))

def home_best_iq(request):
    #sleep(0.5)
    home_best_iq = get_cached_promotion_data('home_best_iq')
    logging.debug(str(home_best_iq))
    return render_to_response('home/home_best_iq.html',
        {'home_best_iq':home_best_iq},
        context_instance=RequestContext(request))

def home_best_riddle(request):
    #sleep(0.5)
    home_best_riddle = get_cached_promotion_data('home_best_riddle')
    return render_to_response('home/home_best_riddle.html',
        {'home_best_riddle':home_best_riddle},
            context_instance=RequestContext(request))
    
def digg(request, type, id):
    """type暂时没检测"""
    if not type:
        return HttpResponse()
    try:
        type = int(type)
    except ValueError:
        raise Http404
    if not id:
        return HttpResponse()
    try:
        id = int(id)
    except ValueError:
        raise Http404
#    data = Content.gql('WHERE type=:1 and key.id=:2', type, id)
    data = Content.get_by_id(id)
    if not data:
        raise Http404
    data.good_score += 1
    data.put()
    return HttpResponse()

def bury(request, type, id):
    """type暂时没检测"""
    if not type:
        return HttpResponse()
    try:
        type = int(type)
    except ValueError:
        raise Http404
    if not id:
        return HttpResponse()
    try:
        id = int(id)
    except ValueError:
        raise Http404
#    data = Content.gql('WHERE type=:1 and key.id=:2', type, id)
    data = Content.get_by_id(id)
    if not data:
        raise Http404
    data.bad_score += 1
    data.put()
    return HttpResponse()
