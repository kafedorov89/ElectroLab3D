# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models
from django import forms
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django.utils.text import Truncator
from django.utils.html import escape


@admin.register (models.Workplace)
class WorkplaceAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['name', 'wp_type', 'url']}),
    ]

    list_display = ('name', 'wp_type', 'url')


@admin.register (models.WpParam)
class WpParamAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['workplace', 'name', 'wp_param_type', 'code', 'device_type', 'device_address', 'source', 'type_func', 'type', 'async']}),
    ]

    list_display = ('workplace', 'name', 'wp_param_type', 'code', 'device_type', 'device_address', 'source', 'type_func', 'type', 'async')


class CourseFieldKeyRawIdWidget (ForeignKeyRawIdWidget):
    def label_for_value(self, value):
        key = self.rel.get_related_field().name
        try:
            obj = self.rel.to._default_manager.select_related('type').using(self.db).get(**{key: value})
            return '&nbsp;<strong>%s</strong>' % escape(Truncator(obj).words(14, truncate = '...'))
        except (ValueError, self.rel.to.DoesNotExist):
            return ''


class CourseFieldForm (forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super (CourseFieldForm, self).__init__ (*args, **kwargs)
        self.fields ['wp_param'].queryset = models.WpParam.objects.all ().select_related ('workplace')
        self.fields ['type'].queryset = models.FieldType.objects.all ().select_related ()

    class Meta:
        model = models.CourseField
        fields = '__all__'


class CourseFieldInline (admin.TabularInline):

    model = models.CourseField
    form = CourseFieldForm
    fk_name = 'course'
    list_display = ('get_course', 'name', 'type', 'wp_param', 'number', 'in_course', 'in_report')
    extra = 0

    def get_queryset(self, request):
        return models.CourseField.objects.filter().select_related ('type')


@admin.register (models.Course)
class CourseAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'Заголовок', {'fields': ['name']}),
        (u'Параметры', {'fields': ['user', 'duration']}),
    ]

    list_display = ('name', 'user', 'duration')
    inlines = [CourseFieldInline, ]


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


@admin.register (models.DeviceType)
class DeviceTypeAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['name']}),
    ]

    list_display = ('name',)


@admin.register (models.FuncType)
class FuncTypeAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['name']}),
    ]

    list_display = ('name',)


@admin.register (models.DataType)
class DataTypeAdmin (admin.ModelAdmin):
    fieldsets = [
        (u'', {'fields': ['name']}),
    ]

    list_display = ('name',)

