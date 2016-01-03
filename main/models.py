# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class WpType (models.Model):
    name = models.CharField (max_length = 200)

    def __unicode__ (self):
        return self.name


class Workplace (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")
    wp_type = models.ForeignKey (WpType, verbose_name = u"Тип")
    url = models.CharField (max_length = 200, default = '', verbose_name = u"Адрес")

    class Meta:
        verbose_name = u"Стенд"
        verbose_name_plural = u"Стенды"

    def __unicode__ (self):
        return u"{} url: {}".format (self.name, self.url)


class WpParamType (models.Model):
    name = models.CharField (max_length = 200)

    def __unicode__ (self):
        return self.name


class DeviceType (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")

    def __unicode__ (self):
        return u"{}".format (self.name, self.id)

    class Meta:
        verbose_name = u"Тип устройства"
        verbose_name_plural = u"Типы устройства"


class FuncType (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")

    def __unicode__ (self):
        return u"{}".format (self.name, self.id)

    class Meta:
        verbose_name = u"Тип функции"
        verbose_name_plural = u"Типы функции"


class DataType (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")

    def __unicode__ (self):
        return u"{}".format (self.name, self.id)

    class Meta:
        verbose_name = u"Тип данных"
        verbose_name_plural = u"Типы данных"


class WpParam (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")
    wp_param_type = models.ForeignKey (WpParamType, verbose_name = u"Тип")
    workplace = models.ForeignKey (Workplace, verbose_name = u"Стенд")
    code = models.CharField (max_length = 200, default = '', verbose_name = u"Код")
    device_type = models.ForeignKey (DeviceType, null = True, blank = True, verbose_name = u"Тип устройства")
    device_address = models.CharField (max_length = 200, default = '', verbose_name = u"Адресс устройства")
    source = models.CharField (max_length = 200, default = '', verbose_name = u"Источник")
    type_func = models.ForeignKey (FuncType, null = True, blank = True, verbose_name = u"Тип функции")
    type = models.ForeignKey (DataType, null = True, blank = True, verbose_name = u"Тип данных")
    async = models.CharField (max_length = 200, default = '', verbose_name = u"Флаг асинхронности")

    def __unicode__ (self):
        return u"{} {} {} id:{}".format (self.workplace.name, self.name, self.code, self.id)

    class Meta:
        verbose_name = u"Параметр стенда"
        verbose_name_plural = u"Параметры стенда"


class Course (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")
    user = models.ForeignKey (User, verbose_name = u"Преподаватель")
    duration = models.DurationField (verbose_name = u"Время на выполнение")

    def __unicode__ (self):
        return self.name

    class Meta:
        verbose_name = u"Лабораторная работа"
        verbose_name_plural = u"Лабораторнаые работы"
        ordering = ('-name',)


class Method (models.Model):
    course = models.ForeignKey (Course, verbose_name = u"Лабораторная работа")
    text_question = models.TextField (verbose_name = u"Текст")

    class Meta:
        verbose_name = u"Методические материалы"
        verbose_name_plural = u"Методические материалы"


class FieldType (models.Model):
    name = models.CharField (max_length = 200)
    code = models.CharField (max_length = 200, default = '')

    def __unicode__ (self):
        return self.name


class CourseField (models.Model):
    course = models.ForeignKey (Course, default = 1, verbose_name = u"Лабораторная работа")
    wp_param = models.ForeignKey (WpParam, null = True, verbose_name = u"UID", blank = True)
    type = models.ForeignKey (FieldType, verbose_name = u"Тип поля")
    name = models.CharField (max_length = 200, verbose_name = u"Заголовок", blank = True)
    param1 = models.TextField (null = True, verbose_name = u"Параметр 1", blank = True)
    param2 = models.TextField (null = True, verbose_name = u"Параметр 2", blank = True)
    param3 = models.TextField (null = True, verbose_name = u"Параметр 3", blank = True)
    number = models.IntegerField (default = 1, null = True, verbose_name = u"Сортировка")
    in_course = models.NullBooleanField (default = True, null = True, verbose_name = u"Отображение в лабораторной")
    in_report = models.NullBooleanField (default = True, null = True, verbose_name = u"Отображение в отчете")
    min_right = models.DecimalField (max_digits = 14, null = True, decimal_places = 4, default = 0, verbose_name = u"Минимальное правильное значение")
    max_right = models.DecimalField (max_digits = 14, null = True, decimal_places = 4, default = 0, verbose_name = u"Максимальное правильное значение")

    class Meta:
        verbose_name = u"Поле лабораторной"
        verbose_name_plural = u"Поля лабораторных"
        ordering = ('-course', 'number')

    def __unicode__ (self):
        return u"{} тип: {} сортировка: {} id:{}".format (self.name, self.type.name, self.number, self.id)


class UserFieldParam (models.Model):
    field = models.ForeignKey (CourseField)
    user = models.ForeignKey (User)
    value = models.TextField (null = True, blank = True)

    class Meta:
        unique_together = ('field', 'user',)


class CourseState (models.Model):
    name = models.CharField (max_length = 200)


class UserCourseState (models.Model):
    course = models.ForeignKey (Course)
    user = models.ForeignKey (User)
    last_date = models.DateTimeField (default = datetime.now)
    course_state = models.ForeignKey (CourseState)

    class Meta:
        unique_together = ('course', 'user',)


class Question (models.Model):
    course = models.ForeignKey (Course, verbose_name = u"Лабораторная работа")
    text_question = models.TextField (verbose_name = u"Текст вопроса")
    number = models.IntegerField (default = 1, verbose_name = u"Сортировка")

    class Meta:
        verbose_name = u"Входной контроль"
        verbose_name_plural = u"Входной контроль"
        ordering = ('-course', 'number')


class Answer (models.Model):
    question = models.ForeignKey (Question, verbose_name = u"Вопрос")
    text_answer = models.TextField (verbose_name = u"Текст ответа")
    right = models.BooleanField (default = False, verbose_name = u"Является верным")

    class Meta:
        verbose_name = u"Ответ"
        verbose_name_plural = u"Ответы"

    def __unicode__ (self):
        return self.text_answer

class UserAnswer (models.Model):
    user = models.ForeignKey (User)
    question = models.ForeignKey (Question)
    answer = models.ForeignKey (Answer)


class UserAllowance (models.Model):
    user = models.ForeignKey (User)
    course = models.ForeignKey (Course)
    construct = models.BooleanField (default = False)
    course_start = models.BooleanField (default = False)
    report = models.BooleanField (default = False)


''' Таблицы для 3Д тренингов '''
class Standtask (models.Model):
    standtask_name = models.CharField (max_length = 200)
    conn_json = models.TextField ()
    rope_json = models.TextField ()

class Standtask_state (models.Model):
    standtask = models.ForeignKey (Standtask)
    user = models.ForeignKey (User)
    user_rope_json = models.TextField ()
    activate = models.BooleanField ()
    complete = models.BooleanField ()
    error = models.BooleanField ()

class Training_log (models.Model):
    user = models.ForeignKey (User)
    training_id = models.IntegerField ()
    training_name = models.CharField (max_length = 200)
    start_time = models.DateTimeField ()
    end_time = models.DateTimeField ()
    complete = models.BooleanField ()
    event_list = models.TextField ()

class Training_param_state (models.Model):
    bool_value = models.BooleanField ()
    int_value = models.IntegerField ()
    training_id = models.IntegerField ()
    session_id = models.IntegerField ()
    float_value = models.DecimalField (max_digits = 14, decimal_places = 4, default = 0)
    string_value = models.TextField ()
    vector3_value = models.TextField ()
    vector2_value = models.TextField ()

class Training_state (models.Model):
    training_id = models.IntegerField ()
    user = models.ForeignKey (User)
    online = models.BooleanField ()
    activate = models.BooleanField ()


