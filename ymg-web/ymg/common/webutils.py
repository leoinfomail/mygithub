#coding=utf8
import base64
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext
from django.template import loader
from ymg.common.paginator import InvalidPage
from ymg.common.paginator import Paginator
# use django1.0 lib

#from Crypto.Cipher import DES
#DES_ID_KEY = 'e9da2cb3'
#crypter4id = DES.new(DES_ID_KEY)
#    cbin = crypter4id.encrypt(str_id)
#    return binascii.b2a_hex(cbin)

def object_list_page(request, queryset, per_page, template_name, page=None, extra_context=None, template_object_name='object', mimetype=None):
    """
    per_page:每页显示数
    page:当前页
    template_name:对应需要render的模板
    extra_context:额外的context
    template_object_name:页面上使用的变量名
    """
    if per_page:
        paginator = Paginator(queryset, per_page)
        if not page:
            # 如果没有传入参数，从request取，默认1
            page = request.GET.get('page', 1)
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages # total
            else:
                # Page is not 'last', nor can it be converted to an int.
                raise Http404
        try:
            page_obj = paginator.page(page_number) # 取得这一页的数据
        except InvalidPage:
            raise Http404
        c = RequestContext(request, {
            'paginator': paginator, #
            'per_page': paginator.per_page, # 每页显示数
            'pages': paginator.num_pages, #总页数
            'counts': paginator.count, #对象总数
            'page_range': paginator.page_range, # page index的范围
            '%s_list' % template_object_name: page_obj.object_list, #模板上使用的变量名，默认object_list
            'page_obj': page_obj, # 这一页的数据对象
            'has_other_pages': page_obj.has_other_pages(),
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'page': page_obj.number, # 当前页的page index
            'previous': page_obj.previous_page_number(), # 上一页的page index
            'next': page_obj.next_page_number(),
            'start_index': page_obj.start_index(), #本页上开始的object在总数上的index
            'end_index': page_obj.end_index(),
        }, None)
    else:
        # 直接抛异常么好了
        raise Http404
    for key, value in extra_context.items():
        if callable(value):
            c[key] = value()
        else:
            c[key] = value
    t = loader.get_template(template_name)
    return HttpResponse(t.render(c), mimetype=mimetype)

class YmgCrypter:
    """ymg的加解密器。不能使用DES，暂时使用base64伪加密。"""
    id_prefix = 'ymgid'
    def encrypt_id(self, id):
        """id不能超过8位，不能为整型以外的任何值"""
        if id > 99999999:
            return '0'
        str_id = str(id)
        id_len = len(str_id)
        add_len = 8 - id_len
        if add_len > 0:
            str_id = ('0' * add_len + str_id)
        return base64.b64encode(self.id_prefix + str_id)
    def decrypt_id(self, cstr):
        """返回整型，解析失败则抛出异常"""
        prefix_str_id = base64.b64decode(cstr)
        str_id = prefix_str_id[5:]
        id = str_id.lstrip('0')
        return int(id)

ymg_crypter = YmgCrypter()

def id2cstr(id):
    """id为整型，返回值为加密后的字符串"""
    return ymg_crypter.encrypt_id(id)

def cstr2id(cstr):
    """返回的为整型"""
    try:
        return ymg_crypter.decrypt_id(cstr)
    except Exception:
        return 1

