# -*- coding: utf-8 -*-
from django.http import *
from django.contrib.auth import login, logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from datetime import datetime
from .models import Course, Question, Answer, UserCourseState, CourseField, Method, UserAnswer, UserAllowance
import functools
from django.shortcuts import redirect


def private (request_number = 0):
    '''
    Декоратор, делат метод доступным только после авторизации.
    В противном случае отсылает на форму авторизации
    :param request_number - номер параметра запроса
    '''
    def _wrap (method):
        @functools.wraps (method)
        def _wrapped (*args, **kwargs):
            try:
                request = args [request_number]
                if request.user.is_authenticated ():
                    return method (*args, **kwargs)
                else:
                    return redirect('/')
            except:
                raise
        return _wrapped
    return _wrap


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
        if self.request.user.is_staff:
            LoginFormView.success_url = "/teacher_main_menu"
        return super (LoginFormView, self).form_valid (form)


class LogoutView (View):
    def get (self, request):
        logout (request)
        return HttpResponseRedirect ("/")


@private()
def main_menu (request):
    current_user = request.user
    templ_data = {
        'first_name' : current_user.first_name,
        'last_name' : current_user.last_name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
    }
    return render_to_response ('main_menu.html', templ_data)


@private()
def timetable (request):
    templ_data = {
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'data' : UserCourseState.objects.select_related ().filter (user = request.user.id).order_by('course_state__name', 'course__name'),
    }
    return render_to_response ('timetable.html', templ_data)


@private()
def timetable_editor (request):
    templ_data = {
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'data' : UserCourseState.objects.select_related ().filter ().order_by('user__id', 'course__name', 'course_state__name'),
    }
    return render_to_response ('timetable_editor.html', templ_data)


@private()
def media_course (request):
    templ_data = {
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'db' : Method.objects.all (),
    }
    return render_to_response ('media_course.html', templ_data)


@private()
def input_control (request, course_id, number):
    number = int (number)
    course_id = int (course_id)
    current_user = request.user
    count = len (list (Question.objects.filter (course = course_id)))
    question = list (Question.objects.filter (course = course_id, number = number)) [0]
    answers = Answer.objects.filter (question = question.id)
    uanswer = UserAnswer.objects.filter (user = current_user, question = question)
    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = current_user, course = course)

    if uanswer:
        uanswer = list (uanswer) [0]
    templ_data = {
        'input_control' : True,
        'host' : request.get_host(),
        'id': course_id,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'pq_id' : number - 1 if number > 1 else None,
        'nq_id' : number + 1 if number < count else None,
        'question' : question,
        'answers' : answers,
        'user' : current_user,
        'uanswer' : uanswer,
        'uallowance' : uallowance,
    }
    return render_to_response ('input_control.html', templ_data)


@private()
def workplace_construct (request, course_id):
    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = request.user, course = course)
    templ_data = {
        'workplace_construct' : True,
        'id': course_id,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'user' : request.user,
        'host' : request.get_host(),
        'uallowance' : uallowance,
    }
    return render_to_response ('workpalce_construct.html', templ_data)


@private()
def course (request, course_id):
    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = request.user, course = course)
    templ_data = {
        'course' : True,
        'controls' : CourseField.objects.select_related ().filter (course__id = course_id).order_by('number', 'id'),
        'id': course_id,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'uallowance' : uallowance,
        'rows' : range(10),
        'rows_select' : range(0, 16),
        'row_cnt' : 10,
    }
    return render_to_response ('course.html', templ_data)


@private()
def report (request, course_id):
    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = request.user, course = course)
    templ_data = {
        'report' : True,
        'db' : CourseField.objects.select_related ().filter (course__id = course_id),
        'id': course_id,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'uallowance' : uallowance,
    }
    return render_to_response ('report.html', templ_data)


@private()
def method (request, course_id):
    templ_data = {
        'id': course_id,
        'db' : list (Method.objects.filter (course__id = course_id)) [0],
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
    }
    return render_to_response ('method.html', templ_data)


@private()
def teacher_main_menu (request):
    current_user = request.user
    templ_data = {
        'first_name' : current_user.first_name,
        'last_name' : current_user.last_name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
    }
    return render_to_response ('teacher_main_menu.html', templ_data)



def load_answer (request, user_id, question_id, answer_id):
    user = User.objects.get (pk = int (user_id))
    question = Question.objects.get (pk = int (question_id))
    answer = Answer.objects.get (pk = int (answer_id))

    column = {
        'user' : user,
        'question' : question,
        'answer' : answer,
    }
    UserAnswer.objects.update_or_create (user = user, question = question, defaults = column)
    return render_to_response ('empty.html')


def check_answer (request, course_id, user_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))

    cnt_question = Question.objects.filter (course = course).count ()
    cnt_user_answer = UserAnswer.objects.filter (user = request.user, question__course = course).count ()
    cnt_bad_user_answer = UserAnswer.objects.filter (user = request.user, question__course = course, answer__right = 0).count ()

    uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)

    if cnt_question == cnt_user_answer and cnt_bad_user_answer == 0:
        uallowance.construct = 1
    else:
        uallowance.construct = 0
        uallowance.course_start = 0
        uallowance.report = 0

    uallowance.save()
    return render_to_response ('empty.html')


def check_workplace (request, course_id, user_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)
    uallowance.course_start = 1
    uallowance.save()
    return render_to_response ('empty.html')


def start_workplace (request, course_id, user_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)
    uallowance.course_start = 0
    uallowance.save()
    return render_to_response ('empty.html')
