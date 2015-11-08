# -*- coding: utf-8 -*-
from models import course
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
#        return reverse('course', args = [course.id])
        return '/input_control/%s/' % (course.id,)

class MethodColumn(Column):
    def __init__(self, *args, **kwargs):
        Column.__init__(self, *args, **kwargs)
        self.link = True
        self.link_func = self.link_to_object

    def render_data(self, state, group):
        return u"Открыть"

    def link_to_object(self, state, course, value):
#        return reverse('method', args = [course.id])
        return '/method/%s/' % (course.id,)


class CoursesDataGrid (DataGrid):
    name = Column (u"Наименование лабораторной работы")
    theacher = Column (u"Преподаватель")
    date = DateTimeColumn (u"Дата/Время")
    date_long = Column (u"Длительность")
    state = Column (u"Статус")
    metod = MethodColumn (u"Методические материалы", link = True)
    start = CourseColumn (u"Приступить к выполнению", link = True)


    def __init__(self, request):
            DataGrid.__init__(self, request, queryset = course.objects.all(), title = "")
            self.default_sort = ['name']
            self.default_columns = ['name', 'theacher', 'date', 'date_long', 'state', 'metod', 'start']
