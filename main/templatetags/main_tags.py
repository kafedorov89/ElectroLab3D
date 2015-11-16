# -*- coding: utf-8 -*-
from django.template import Library


register = Library()

@register.filter(name = 'column_range')
def column_range (number):
    return range (int (number))
