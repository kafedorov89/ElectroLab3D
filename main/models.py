# -*- coding: utf-8 -*-
from django.db import models


class wp_type (models.Model):
    name = models.CharField (max_length = 200)


class workplace (models.Model):
    name = models.CharField (max_length = 200)
    wp_type = models.ForeignKey (wp_type)


class wp_param_type (models.Model):
    name = models.CharField (max_length = 200)


class wp_param (models.Model):
    name = models.CharField (max_length = 200)
    wp_param_type = models.ForeignKey (wp_param_type)
    workplace = models.ForeignKey (workplace)


class wp_preset (models.Model):
    name = models.CharField (max_length = 200)
    value = models.IntegerField (default = 0)
    workplace = models.ForeignKey (workplace)
    wp_param = models.ForeignKey (wp_param)


class wp_user (models.Model):
    value = models.IntegerField (default = 0)
#    user = models.ForeignKey (user)
    workplace = models.ForeignKey (workplace)
    wp_param = models.ForeignKey (wp_param)


class wp_action (models.Model):
    priority = models.IntegerField (default = 0)
    workplace = models.ForeignKey (workplace)
    wp_param = models.ForeignKey (wp_param)


class course (models.Model):
    name = models.CharField (max_length = 200)
    last_date = models.DateTimeField ()

