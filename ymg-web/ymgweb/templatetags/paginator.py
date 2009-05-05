#coding=utf8
"""
从context中取得数据，重新组织后放入新的context，新的context对应到tag的模板上
原先的context是使用object_list_page放入context中的
http://www.djangosnippets.org/snippets/73/
"""

from django.template import Library

register = Library()

@register.inclusion_tag('common/tags/paginator.html', takes_context=True)
def paginator(context, adjacent_pages=5):
    #per_page = context['per_page']
    #left_results= context['counts'] - context['end_index']
    #next_per_page = left_results < per_page and left_results or per_page

    page_numbers = [n for n in range(context['page'] - adjacent_pages, context['page'] + adjacent_pages + 1) if n > 0 and n <= context['pages']]
    ctx = {
        'page_numbers': page_numbers,
        'counts': context['counts'],
        'per_page': context['per_page'],
        'page': context['page'],
        'pages': context['pages'],
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
        #'next_per_page': next_per_page,  ???
    }
    # 额外的变量，控制页面生成内容，如url
    if context.has_key('url_prefix'):
        ctx['url_prefix'] = context['url_prefix']
    return ctx
