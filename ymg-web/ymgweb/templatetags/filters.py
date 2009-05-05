#coding=utf8
"""
filter的几种实现：
内容：
1，根据长度比如100，判断最后的p出现在哪里，p内部不切换。
如果最后的半个p很长，导致结果很短。反过来说，需要这最后的p，则超出长度将不可预计
2，以p为单位，check长度，p内部不切换。首先查看2个p的长度是否超出，超出则停止。最多显示4个p。
标题：
严格限制长度
"""
from django.http import Http404
from django.template import Library
from django.template.defaultfilters import stringfilter
from ymg.common.webutils import id2cstr

register = Library()

@register.filter(name='simple_truncate')
@stringfilter
def simple_truncate(str, length=None):
    """去掉p标签，如果有length且超长则强制切断加..."""
    more = u'...'
    str = str.replace(u'<p>', u'')
    str = str.replace(u'</p>', u' ')
    str = str.strip()
    if not length or len(str) < length:
        return str
    return str[:length] + more

@register.filter(name='simple_truncate_no_scope')
@stringfilter
def simple_truncate_no_scope(str, length=None):
    """同simple_truncate，去掉[xx]"""
    more = u'...'
    str = str.replace(u'<p>', u'')
    str = str.replace(u'</p>', u' ')
    str = str.strip()
    index = str.rfind('[')
    str = str[:index]
    if not length or len(str) < length:
        return str
    return str[:length] + more

@register.filter
@stringfilter
def strict_truncate_to(str, length=None):
    """去掉html标签，如果有length且超长则强制切断"""
    more = u'...'
    str = str.replace(u'\n', u'')
    str = str.replace(u'<p>', u'')
    str = str.replace(u'</p>', u' ')
    if len(str) < length:
        return str
    return str[:length] + more

@register.filter(name='list_truncate')
@stringfilter
def list_truncate(str):
    """以每加一段是否超过round_length来判断，先添上......，再想办法加上链接"""
    round_length = 200
    more = u'<p>... ...</p>'
    p1 = str.find(u'</p>')
    p2 = str.find(u'</p>', p1 + 4)
    if p1 > round_length:
        if p2 != -1:
            return str[:p1 + 4] + more
        else:
            return str[:p1 + 4]
    elif p2 == -1:
        return str
    #
    p3 = str.find(u'</p>', p2 + 4)
    if p2 > round_length:
        if p3 != -1:
            return str[:p2 + 4] + more
        else:
            return str[:p2 + 4]
    elif p3 == -1:
        return str[:p2 + 4]
    #
    p4 = str.find(u'</p>', p3 + 4)
    if p3 > round_length:
        if p4 != -1:
            return str[:p3 + 4] + more
        else:
            return str[:p3 + 4]
    elif p4 == -1:
        return str[:p3 + 4]
    #
    p5 = str.find(u'</p>', p4 + 4)
    if p5 != -1:
        return str[:p4 + 4] + more
    else:
        return str[:p4 + 4]

@register.filter
@stringfilter
def id_to_cstr(id):
    try:
        id = int(id)
    except Exception:
        raise Http404
    return id2cstr(id)
