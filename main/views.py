# -*- coding: utf-8 -*-
from django.http import *
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime
from courses import CoursesDataGrid


class EUserCreationForm(UserCreationForm):
    def __init__ (self, *args, **kwargs):
        super (EUserCreationForm, self).__init__ (*args, **kwargs)
        self.fields ['username'].label = u'Логин'

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class RegisterFormView (FormView):
    form_class = EUserCreationForm

    template_name = "register.html"
    success_url = "/login"

    def form_valid (self, form):
        form.save ()
        return super (RegisterFormView, self).form_valid (form)


class EAuthenticationForm (AuthenticationForm):
    def __init__ (self, request = None, *args, **kwargs):
        super (EAuthenticationForm, self).__init__ (request, *args, **kwargs)
        self.fields['username'].label = u'Логин:'
        self.fields['password'].label = u'Пароль:'


class LoginFormView (FormView):
    form_class = EAuthenticationForm

    template_name = "login.html"
    success_url = "/main_menu"

    def form_valid (self, form):
        self.user = form.get_user ()
        login (self.request, self.user)
        return super (LoginFormView, self).form_valid (form)


class LogoutView (View):
    def get (self, request):
        logout (request)
        return HttpResponseRedirect ("/")


def main_menu (request):
    current_user = request.user
    templ_data = {
        'first_name' : current_user.first_name,
        'last_name' : current_user.last_name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
    }
    return render_to_response ('main_menu.html', templ_data)

def timetable (request):
    templ_data = {
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
    }
    return CoursesDataGrid (request).render_to_response ('timetable.html', templ_data)

def media_course (request):
    current_user = request.user
    templ_data = {
    }
    return render_to_response ('media_course.html', templ_data)

