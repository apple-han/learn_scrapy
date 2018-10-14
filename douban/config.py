# -*- coding: utf-8 -*-
# @Time    : 2018/10/4 上午8:41
# @Author  : __apple

def from_object(obj):
    d = dict()
    for key in dir(obj):
        if key.isupper():
            d[key.lower()] = getattr(obj, key)

    return d