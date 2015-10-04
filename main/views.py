# -*- coding: utf-8 -*-

from django.http import *
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.template import RequestContext


class RegisterFormView (FormView):
    form_class = UserCreationForm

    template_name = "register.html"
    success_url = "/login"

    def form_valid (self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save ()

        # Вызываем метод базового класса
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
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user ()

        # Выполняем аутентификацию пользователя.
        login (self.request, self.user)
        return super (LoginFormView, self).form_valid (form)


class LogoutView(View):
    def get (self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout (request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect ("/")


def main_menu(request):
    return render_to_response('main_menu.html', context_instance = RequestContext(request))

