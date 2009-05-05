#coding=utf8
from random import shuffle

from django.template import Library
from ymgweb.utils import get_cached_promotion_data
from ymgweb.utils import get_one_iq_static_info_link
from ymgweb.utils import get_one_riddle_static_info_link

register = Library()

"""每一类的显示统一，数据源由py控制"""
@register.inclusion_tag('common/tags/humor_acd.html', takes_context=True)
def humor_acd(context):
    humor_acd = get_cached_promotion_data('detail_acd_humor')
    shuffle(humor_acd)
    context['humor_acd'] = humor_acd
    return context

@register.inclusion_tag('common/tags/iq_acd.html', takes_context=True)
def iq_acd(context):
    iq_acd = get_cached_promotion_data('detail_acd_iq')
    shuffle(iq_acd)
    context['iq_acd'] = iq_acd
    return context

@register.inclusion_tag('common/tags/riddle_acd.html', takes_context=True)
def riddle_acd(context):
    riddle_acd = get_cached_promotion_data('detail_acd_riddle')
    shuffle(riddle_acd)
    context['riddle_acd'] = riddle_acd
    return context

@register.inclusion_tag('common/tags/cm_bg_rnd_static_info.html', takes_context=True)
def riddle_static_info(context):
    (title, link) = get_one_riddle_static_info_link()
    context['title'] = title
    context['link'] = link
    return context

@register.inclusion_tag('common/tags/cm_bg_rnd_static_info.html', takes_context=True)
def iq_static_info(context):
    (title, link) = get_one_iq_static_info_link()
    context['title'] = title
    context['link'] = link
    return context
