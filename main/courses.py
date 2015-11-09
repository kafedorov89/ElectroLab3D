# -*- coding: utf-8 -*-
from models import Course
from djblets.datagrid.grids import Column, DataGrid, DateTimeColumn
from django.core.urlresolvers import reverse

class CourseColumn(Column):
    def __init__(self, *args, **kwargs):
        Column.__init__(self, *args, **kwargs)
        self.link = True
        self.link_func = self.link_to_object

    def render_data(self, state, group):
        return u"Приступить"

    def link_to_object(self, state, course, value):
        return '/input_control/%s/1/' % (course.id,)

class MethodColumn(Column):
    def __init__(self, *args, **kwargs):
        Column.__init__(self, *args, **kwargs)
        self.link = True
        self.link_func = self.link_to_object

    def render_data(self, state, group):
        return u"Открыть"

    def link_to_object(self, state, course, value):
        return '/method/%s/' % (course.id,)


class CoursesDataGrid (DataGrid):
    name = Column (u"Наименование лабораторной работы")
    theacher = Column (u"Преподаватель")
    last_date = DateTimeColumn (u"Дата/Время")
    duration = Column (u"Длительность")
    state = Column (u"Статус")
    metod = MethodColumn (u"Методические материалы", link = True)
    start = CourseColumn (u"Приступить к выполнению", link = True)


    def __init__(self, request):
            qs = Course.objects.select_related()
            DataGrid.__init__(self, request, queryset = qs, title = "")
            self.default_sort = ['name']
            self.default_columns = ['name', 'theacher', 'last_date', 'duration', 'state', 'metod', 'start']
