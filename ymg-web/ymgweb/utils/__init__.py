#coding=utf8
from ymgweb.utils.static_info import iq_static_info
import random

from google.appengine.api import memcache
from ymgweb.content.models import Content
from ymgweb.manage.models import Promotion
from ymgweb.utils.static_info import riddle_static_info

def get_cached_promotion_data(promotion_subject, time=6000):
    """
    使用规则的名称获得缓存的数据list。
    TODO 应该做类型检查！
    """
    cached_data = memcache.get(promotion_subject)
    if not cached_data:
        promotion = Promotion.all().filter('subject', promotion_subject)
        cached_data_ids = []
        for item in promotion:
            cached_data_string_ids_str = item.content.split(',')
            for id_str in cached_data_string_ids_str:
                try:
                    id = int(id_str)
                except Exception:
                    continue
                if id > 0:
                    cached_data_ids.append(id)
        temp_cached_data = Content.get_by_id(cached_data_ids)
        cached_data = [data for data in temp_cached_data if data is not None]
        memcache.set(promotion_subject, cached_data, time)
    return cached_data

#        model = promotion_subject.rsplit('_', 1)[-1]
#        if model == 'humor':
#            temp_cached_data = Humor.get_by_id(cached_data_ids)
#        elif model == 'iq':
#            temp_cached_data = Iq.get_by_id(cached_data_ids)
#        elif model == 'riddle':
#            temp_cached_data = Riddle.get_by_id(cached_data_ids)

def get_one_cached_promotion_data(promotion_subject):
    """从推荐数据中随机取一条"""
    cached_data = get_cached_promotion_data(promotion_subject)
    size = len(cached_data)
    if size > 0:
        return cached_data[random.randint(0, size-1)]
    return None

def get_pre_next_data(current_id, type):
    """史上最龌龊的实现，哈哈"""
    pre_data = None
    pre_id = current_id
    while not pre_data:
        pre_id -= 1
        if pre_id > 0:
            _pre_data = Content.get_by_id(pre_id)
            if _pre_data and _pre_data.type == type:
                pre_data = _pre_data
        if pre_id < current_id - 10:
            break
    next_data = None
    next_id = current_id
    while not next_data:
        next_id += 1
        if next_id > 0:
            _next_data = Content.get_by_id(next_id)
            if _next_data and _next_data.type == type:
                next_data = _next_data
        if next_id > current_id + 10:
            break
    return (pre_data, next_data)

def get_one_riddle_static_info_link():
    """返回一个tuple"""
    size = len(riddle_static_info)
    if size > 1:
        return riddle_static_info[random.randint(1, size-1)]
    else:
        return riddle_static_info[0]
    return ""

def get_one_iq_static_info_link():
    """返回一个tuple"""
    size = len(iq_static_info)
    if size > 1:
        return iq_static_info[random.randint(1, size-1)]
    else:
        return iq_static_info[0]
    return ""
