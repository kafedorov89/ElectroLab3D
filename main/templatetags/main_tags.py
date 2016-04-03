# -*- coding: utf-8 -*-
from django.template import Library


register = Library()

@register.filter(name = 'table_heigth')
def table_heigth (param):
    width = param.split(";") [0]
    return range (int (width))

@register.filter(name = 'table_len_heigth')
def table_len_heigth (param):
    print param
    width = param.split(";") [0]
    if width:
        return int (width)
    return 0

@register.filter(name = 'rep_error')
def rep_error (string):
    if string.find (u'Ошибка!') == -1:
        return 'color: #000000;'
    else:
        return 'color: red;'

@register.filter(name = 'table_width')
def table_width (param):
    params = param.split(";")
    if len (params) > 1:
        return range (int (params [1]))
    else:
        return 0

@register.filter(name = 'table_width_l')
def table_width_l (param):
    params = param.split(";")
    if len (params) > 1:
        return range (int (params [1]) + 1)
    else:
        return 0

@register.filter(name = 'chart_name')
def chart_name (param):
    if param:
        return param.split(";") [0]
    return 'Напряжение'

@register.filter(name = 'all_chart_name')
def all_chart_name (param):
    if param:
        res = []
        res.append(param.split(";") [0])
        if param.split(";")[3:]:
            for name in param.split(";")[3:]:
                res.append(name)
        return ';'.join(res)
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
        if len (params) > int (cur):
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

@register.filter(name = 'get_n')
def get_n (param):
    return param.split(";") [0]

@register.filter(name = 'get_table_uid')
def get_table_uid (param):
    return ';'.join(param.split(";") [1:])

@register.filter(name = 'table_width2')
def table_width2 (param):
    params = param.split(";")
    if len (params) > 2:
        return range (int (params [1]), int (params [1]) + int (params [2]))
    else:
        return 0

@register.filter(name = 'table_width2_l')
def table_width2_l (param):
    params = param.split(";")
    if len (params) > 2:
        return range (int (params [1]) + 1, int (params [1]) + int (params [2]) + 1)
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

import cStringIO as c
import csv

@register.filter(name = 'table_head')
def table_head (param, i):
    head = param.split(";") [0]
    if not head:
        return ''
    head_range = csv.reader(c.StringIO (head.encode ('utf-8')), delimiter = ',', escapechar = '\\').next()
    return head_range [i] if len (head_range) > int(i) else ''

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
    if not head:
        return ''
    if len (head) > 1:
        head_left_range = csv.reader(c.StringIO (head [1].encode ('utf-8')), delimiter = ',', escapechar = '\\').next()
        return head_left_range [i] if len (head_left_range) > int(i) else ''
    else:
        return ''

@register.filter(name = 'swicher_range')
def swicher_range (number):
    if number is None:
        number = 16
    return range (1, int (number) - 1)

from django import template

class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value
        return u""

def set_var(parser, token):
    """
        {% set <var_name>  = <var_value> %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set <var_name>  = <var_value> %}")
    return SetVarNode(parts[1], parts[3])

register.tag('set', set_var)
