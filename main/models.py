# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class WpType (models.Model):
    name = models.CharField (max_length = 200)


class Workplace (models.Model):
    name = models.CharField (max_length = 200)
    wp_type = models.ForeignKey (WpType)
    url = models.CharField (max_length = 200, default = '')


class WpParamType (models.Model):
    name = models.CharField (max_length = 200)


class WpParam (models.Model):
    name = models.CharField (max_length = 200)
    wp_param_type = models.ForeignKey (WpParamType)
    workplace = models.ForeignKey (Workplace)
    code = models.CharField (max_length = 200, default = '')


class Course (models.Model):
    name = models.CharField (max_length = 200)
    last_date = models.DateTimeField ()
    user = models.ForeignKey (User)
    duration = models.DurationField ()


class Method (models.Model):
    course = models.ForeignKey (Course)
    text_question = models.TextField ()


class FieldType (models.Model):
    name = models.CharField (max_length = 200)
    code = models.CharField (max_length = 200, default = '')


class CourseField (models.Model):
    course = models.ForeignKey (Course, default = 1)
    wp_param = models.ForeignKey (WpParam, null = True)
    type = models.ForeignKey (FieldType)
    name = models.CharField (max_length = 200)
    param1 = models.TextField (null = True)
    param2 = models.TextField (null = True)
    param3 = models.TextField (null = True)


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
    course = models.ForeignKey (Course)
    text_question = models.TextField ()
    number = models.IntegerField (default = 1)


class Answer (models.Model):
    question = models.ForeignKey (Question)
    text_answer = models.TextField ()
    right = models.BooleanField (default = False)


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
