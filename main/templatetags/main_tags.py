# -*- coding: utf-8 -*-
from django.template import Library


register = Library()

@register.filter(name = 'table_heigth')
def table_heigth (param):
    width = param.split(";") [0]
    return range (int (width))

@register.filter(name = 'table_len_heigth')
def table_len_heigth (param):
    width = param.split(";") [0]
    return int (width)

@register.filter(name = 'table_width')
def table_width (param):
    params = param.split(";")
    if len (params) > 1:
        return range (int (params [1]))
    else:
        return 0

@register.filter(name = 'chart_name')
def chart_name (param):
    if param:
        return param.split(";") [0]
    return 'Напряжение'

@register.filter(name = 'chart_x')
def chart_x (param):
    if param:
        params = param.split(";")
        if len (params) > 1:
            return param.split(";") [1]
    return 'Время'

@register.filter(name = 'chart_y')
def chart_y (param):
    if param:
        params = param.split(";")
        if len (params) > 2:
            return param.split(";") [2]
    return 'Влт'

@register.simple_tag
def get_table_value (param, width, i, j):
    if param:
        params = param.split(";")
        cur = j + i * width
        if len (params) >= i:
            return params [cur]
    return ''

@register.filter(name = 'data_to_chart')
def data_to_chart (param):
    if param:
        return ','.join (param.split(";"))
    return ''

@register.filter(name = 'param_url')
def param_url (param):
    return param.split(";") [0]

@register.filter(name = 'table_width2')
def table_width2 (param):
    params = param.split(";")
    if len (params) > 2:
        return range (int (params [2]))
    else:
        return 0

@register.filter(name = 'table_len_width')
def table_len_width (param):
    params = param.split(";")
    if len (params) > 1:
        return int (params [1])
    else:
        return 0

@register.filter(name = 'exist_left_head')
def exist_left_head (param):
    head = param.split(";")
    if len (head) > 1:
        return True
    else:
        return False

@register.filter(name = 'table_head')
def table_head (param, i):
    head = param.split(";") [0]
    head_range = head.split(",")
    return head_range [i] if len (head_range) >= int(i) else ''

@register.filter(name = 'multitable_name1')
def multitable_name1 (param):
    name = param.split(";") [0]
    return name

@register.filter(name = 'multitable_name2')
def multitable_name2 (param):
    name = param.split(";")
    return name [1] if len (name) > 1 else ''

@register.filter(name = 'table_left_head')
def table_left_head (param, i):
    head = param.split(";")
    if len (head) > 1:
        head_left_range = head [1].split(",")
        return head_left_range [i] if len (head_left_range) >= int(i) else ''
    else:
        return ''

@register.filter(name = 'swicher_range')
def swicher_range (number):
    if number is None:
        number = 16
    return range (1, int (number) - 1)
