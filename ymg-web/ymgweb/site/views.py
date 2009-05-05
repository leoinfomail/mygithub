#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

def site(request, template):
    if not template:
        return HttpResponseRedirect('/')
    try:
        return render_to_response('site/%s.html' % template, context_instance=RequestContext(request))
    except Exception, e:
        raise Http404
