#coding=utf8
'''各种状态tag'''
from django.template import Library

register = Library()

@register.inclusion_tag('common/tags/user_status.html', takes_context=True)
def user_status(context):
    return context