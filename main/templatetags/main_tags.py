# -*- coding: utf-8 -*-
from django.template import Library


register = Library()

@register.filter(name = 'column_range')
def column_range (number):
    return range (int (number))

@register.filter(name = 'swicher_range')
def swicher_range (number):
    if number is None:
        number = 16
    return range (1, int (number) - 1)