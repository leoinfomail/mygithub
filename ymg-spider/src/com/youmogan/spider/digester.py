#coding=utf8
from com.youmogan.spider.html_helper import regularize_html_content
import htmlentitydefs
import re

def decode_html_entity(data):
    result = data
    pattern_name = r'&(\w{2,8});'
    pattern_code = r'&#(\d{1,3});'

    name_entites = re.findall(pattern_name, data)
    for entity in name_entites:
        if htmlentitydefs.name2codepoint.has_key(entity):
            result = result.replace('&' + entity + ';', unichr(htmlentitydefs.name2codepoint[entity]))

    code_entites = re.findall(pattern_code, data)
    for entity in code_entites:
        result = result.replace('&#' + entity + ';', unichr(int(entity)).encode('utf-8'))
    return result

class Digester(object):
    """
    html解析器
    """
    def search_one_result(self, pattern, data, return_group_index):
        """re.search()查找，并返回指定序号的group"""
        m = re.search(pattern, data, re.DOTALL)
        if m:
            return m.group(return_group_index)
        else:
            return None

    def regularize_content(self, data):
        """规范化输入数据。"""
        if not data:
            return ''
        data = regularize_html_content(data)
        try:
            return decode_html_entity(data)
        except UnicodeDecodeError:
            return None

if __name__ == '__main__':
    data = r'&lt;---&lt;'
    print data
    print decode_html_entity(data)


