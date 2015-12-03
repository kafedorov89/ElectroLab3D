# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


class CourseFieldAdmin (admin.StackedInline):
    fieldsets = [
        (u'', {'fields': ['name', 'course', 'type', 'wp_param']}),
        (u'Параметры', {'fields': ['param1', 'param2', 'param3', 'number', 'in_course', 'in_report']}),
        (u'Контроль', {'fields': ['min_right', 'max_right']}),
    ]

    model = models.CourseField
    extra = 0

    def get_course (self, obj):
        return obj.course.name
    get_course.short_description = u"Лабораторная работа"
    get_course.admin_order_field = 'course__name'

    list_display = ('get_course', 'name', 'type', 'wp_param', 'number', 'in_course', 'in_report')


@admin.register (models.Course)
class CourseAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'Заголовок', {'fields': ['name']}),
        (u'Параметры', {'fields': ['last_date', 'user', 'duration']}),
    ]

    list_display = ('name', 'last_date', 'user', 'duration')

    inlines = [CourseFieldAdmin]


class AnswerInline (admin.StackedInline):
    model = models.Answer
    list_display = ('text_answer', 'right')
    extra = 0


@admin.register (models.Question)
class QuestionAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['course', 'text_question', 'number']}),
    ]

    list_display = ('course', 'text_question', 'number')

    inlines = [AnswerInline]


@admin.register (models.Method)
class MethodAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['course', 'text_question']}),
    ]

    list_display = ('course', 'text_question')


@admin.register (models.Workplace)
class WorkplaceAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['name', 'wp_type', 'url']}),
    ]

    list_display = ('name', 'wp_type', 'url')


@admin.register (models.WpParam)
class WpParamAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['workplace', 'name', 'wp_param_type', 'code']}),
    ]

    list_display = ('workplace', 'name', 'wp_param_type', 'code')

