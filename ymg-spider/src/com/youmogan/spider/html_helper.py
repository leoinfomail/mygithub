#coding=utf8
import re

def regularize_html_content(html):
    """将合法的html片段中的内容转换成以p为分割的规范化内容"""
    #1.将所有html tag转成小写
    html = html.strip()
    raw_html_tags = re.findall(r'</?[^>]+>', html)
    lower_tags = []
    for tags in raw_html_tags:
        lower_tags.append(tags.lower())
    for i in range(len(raw_html_tags)):
        html = html.replace(raw_html_tags[i], lower_tags[i])
    #2.去掉非分段tag
    lower_tags_set = set(lower_tags)
    tmp_tags_list = []
    for tags in lower_tags_set:
        tmp_tags_list.append(tags)
    tmp_tags_string = ''.join(tmp_tags_list)
    p_br = re.findall(r'</?p[^>]*>|<br\s*/?>', tmp_tags_string)
    for item in p_br:
        lower_tags_set.remove(item)
    for item in lower_tags_set:
        html = html.replace(item, '')
    #3.去掉p的样式，去掉br，添加必要的</p>
    p_br = re.findall(r'</?p[^>]*>|<br\s*/?>', html)
    for item in p_br:
        html = html.replace(item, '<ymg-p>')
    raw_list = html.split('<ymg-p>')
    tmp_list = []
    for item in raw_list:
        item_striped = item.strip().strip('　')#可以去掉全角空格
        if item_striped:
            tmp_list.append(item_striped)
    tmp_html = '</p><p>'.join(tmp_list)
    return '<p>' + tmp_html + '</p>'

if __name__ == '__main__':
    html = """
      <TR>
        <TD height=50 valign=top bgcolor="#F6F6F6"> 
          <div align="center">人生多风雨，幽默常相伴！中文幽默王，快乐每一天！把这个网址告诉你的朋友，你会得到两份快乐！<br>
            <br>
            Copyright &copy;2002 - 2005 <font face=Verdana, Arial, Helvetica, sans-serif size=1><b>haha365<font color=#CC0000>.Com</font></b></font></a>   <a href=http://www.miibeian.gov.cn/ target=_blank><font color=#999999>晋ICP备05000110号</font></a> <br>
            <br>
          </div></TD>
    """
    print regularize_html_content(html)