# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


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


class WpParam (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")
    wp_param_type = models.ForeignKey (WpParamType, verbose_name = u"Тип")
    workplace = models.ForeignKey (Workplace, verbose_name = u"Стенд")
    code = models.CharField (max_length = 200, default = '', verbose_name = u"Код")

    def __unicode__ (self):
        return u"{} {} {}".format (self.workplace.name, self.name, self.code)

    class Meta:
        verbose_name = u"Параметр стенда"
        verbose_name_plural = u"Параметры стенда"


class Course (models.Model):
    name = models.CharField (max_length = 200, verbose_name = u"Название")
    last_date = models.DateTimeField (verbose_name = u"Дата")
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
    wp_param = models.ForeignKey (WpParam, null = True, verbose_name = u"UID")
    type = models.ForeignKey (FieldType, verbose_name = u"Тип поля")
    name = models.CharField (max_length = 200, verbose_name = u"Заголовок")
    param1 = models.TextField (null = True, verbose_name = u"Параметр 1")
    param2 = models.TextField (null = True, verbose_name = u"Параметр 2")
    param3 = models.TextField (null = True, verbose_name = u"Параметр 3")
    number = models.IntegerField (default = 1, verbose_name = u"Сортировка")
    in_course = models.BooleanField (default = False, verbose_name = u"Отображение в лабораторной")
    in_report = models.BooleanField (default = False, verbose_name = u"Отображение в отчете")
    min_right = models.DecimalField (max_digits = 14, decimal_places = 4, default = 0, verbose_name = u"Минимальное правильное значение")
    max_right = models.DecimalField (max_digits = 14, decimal_places = 4, default = 0, verbose_name = u"Максимальное правильное значение")

    class Meta:
        verbose_name = u"Поле лабораторной"
        verbose_name_plural = u"Поля лабораторных"
        ordering = ('-course', 'number')

    def __unicode__ (self):
        return u"{} тип: {} сортировка: {}".format (self.name, self.type.name, self.number)


class UserFieldParam (models.Model):
    field = models.ForeignKey (CourseField)
    value = models.CharField (max_length = 200)


class CourseState (models.Model):
    name = models.CharField (max_length = 200)


class UserCourseState (models.Model):
    course = models.ForeignKey (Course)
    user = models.ForeignKey (User)
    course_state = models.ForeignKey (CourseState)


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
class Training (models.Model):
    name = models.CharField (max_length = 200)


class TrainingList (models.Model):
    traning = models.ForeignKey (Training)
    start_time = models.DateTimeField ()
    end_time = models.DateTimeField ()
    traning_status = models.BooleanField ()


class StandTask (models.Model):
    name = models.CharField (max_length = 200)


class StandTaskState (models.Model):
    stand_task = models.ForeignKey (StandTask)
    user = models.ForeignKey (User)
    name = models.CharField (max_length = 200)
    activate = models.BooleanField ()
    complete = models.BooleanField ()
    error = models.BooleanField ()


class TrainingEventLog (models.Model):
    traning = models.ForeignKey (Training)
    user = models.ForeignKey (User)
    name = models.CharField (max_length = 200)
    status = models.BooleanField ()
    time = models.DateTimeField ()
