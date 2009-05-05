#coding=utf8

from django import shortcuts
from django.template import RequestContext

#def render_to_response(template,context={},request):
#    '''deprecated,在启用用户之前，页面不需要关心。在启用用户之后，在views每个render上加context instance
#    不需要的可以不加
#    默认使用RequestContext，激活context processors'''
#    return shortcuts.render_to_response(template,context,
#                                               context_instance=RequestContext(request))
    

