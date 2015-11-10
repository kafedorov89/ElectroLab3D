# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class WpType (models.Model):
    name = models.CharField (max_length = 200)


class Workplace (models.Model):
    name = models.CharField (max_length = 200)
    wp_type = models.ForeignKey (WpType)


class WpParamType (models.Model):
    name = models.CharField (max_length = 200)


class WpParam (models.Model):
    name = models.CharField (max_length = 200)
    wp_param_type = models.ForeignKey (WpParamType)
    workplace = models.ForeignKey (Workplace)


class WpPreset (models.Model):
    name = models.CharField (max_length = 200)
    value = models.IntegerField (default = 0)
    workplace = models.ForeignKey (Workplace)
    wp_param = models.ForeignKey (WpParam)


class WpUser (models.Model):
    value = models.IntegerField (default = 0)
    user = models.ForeignKey (User)
    workplace = models.ForeignKey (Workplace)
    wp_param = models.ForeignKey (WpParam)


class WpAction (models.Model):
    priority = models.IntegerField (default = 0)
    workplace = models.ForeignKey (Workplace)
    wp_param = models.ForeignKey (WpParam)


class Course (models.Model):
    name = models.CharField (max_length = 200)
    last_date = models.DateTimeField ()
    user = models.ForeignKey (User)
    duration = models.DurationField ()


class CourseGroupField (models.Model):
    course = models.ForeignKey (Course)
    name = models.CharField (max_length = 200)


class FieldType (models.Model):
    name = models.CharField (max_length = 200)


class CourseField (models.Model):
    group = models.ForeignKey (CourseGroupField)
    type = models.ForeignKey (FieldType)
    name = models.CharField (max_length = 200)


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

