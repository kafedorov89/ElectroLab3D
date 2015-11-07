# -*- coding: utf-8 -*-
from models import course
from djblets.datagrid.grids import Column, DataGrid

class CoursesDataGrid (DataGrid):
    name = Column (u"Наименование лабораторной работы")
    theacher = Column (u"Преподаватель")
    date = Column (u"Дата/Время")
    date_long = Column (u"Длительность")
    state = Column (u"Статус")
    metod = Column (u"Методические материалы", link = True)
    start = Column (u"Приступить к выполнению", link = True)

    def __init__(self, request):
            DataGrid.__init__(self, request, queryset = course.objects.all(), title = "")
            self.default_sort = ['name']
            self.default_columns = ['name', 'theacher', 'date', 'date_long', 'state', 'metod', 'start']
