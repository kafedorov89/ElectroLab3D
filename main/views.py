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
from .models import Course, Question, Answer, UserCourseState, CourseField, Method, UserAnswer, UserAllowance, CourseState, UserFieldParam, Standtask_state, Standtask
import functools
from django.shortcuts import redirect
from django.http import JsonResponse


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
    question = list (Question.objects.filter (course = course_id, number = number))
    if len (question) == 0:
        answers = []
        uanswer = []
    else:
        question = question [0]
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
        'number': course.name,
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
        'number': course.name,
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
        'controls' : CourseField.objects.select_related ().filter (course__id = course_id, in_course = True).order_by ('number', 'id'),
        'id': course_id,
        'number': course.name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'uallowance' : uallowance,
        'host' : request.get_host(),
        'user' : request.user,
    }
    return render_to_response ('course.html', templ_data)


@private()
def report (request, course_id):
    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = request.user, course = course)
    templ_data = {
        'report' : True,
        'controls' : UserFieldParam.objects.select_related ().filter (user = request.user, field__course__id = course_id, field__in_report = True),
        'id': course_id,
        'number': course.name,
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


@private()
def course_state_add (request, student, course, date, state):
    obj_date = datetime.strptime(date, '%d.%m.%Y').date ()
    obj_course = Course.objects.get (pk = course)
    obj_course_state = CourseState.objects.get (pk = state)
    obj_user = User.objects.get (pk = student)
    UserCourseState.objects.update_or_create (user = obj_user, course = obj_course, last_date = obj_date, course_state = obj_course_state)
    return HttpResponseRedirect ("/timetable_editor/")


@private()
def course_state_cng (request, id, student, course, date, state):
    obj_date = datetime.strptime(date, '%d.%m.%Y').date ()
    obj_course = Course.objects.get (pk = course)
    obj_course_state = CourseState.objects.get (pk = state)
    obj_user = User.objects.get (pk = student)
    UserCourseState.objects.filter (pk = id).update (user = obj_user, course = obj_course, last_date = obj_date, course_state = obj_course_state)
    return HttpResponseRedirect ("/timetable_editor/")


@private()
def course_state_del (request, id):
    UserCourseState.objects.get (pk = id).delete ()
    return HttpResponseRedirect ("/timetable_editor/")


@private()
def course_state_form (request, action, id = None):
    current_user = request.user
    students = User.objects.select_related ().filter ().order_by('last_name', 'first_name')
    courses = Course.objects.select_related ().filter ().order_by('id')
    states = CourseState.objects.select_related ().filter ()

    cur_course = None
    last_date = None
    if id is not None:
        cur_course = UserCourseState.objects.get (pk = int (id))
        last_date = cur_course.last_date.strftime("%d.%m.%Y")

    templ_data = {
        'first_name' : current_user.first_name,
        'last_name' : current_user.last_name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'students' : students,
        'courses' : courses,
        'states' : states,
        'action' : action,
        'id' : id,
        'cur_course' : cur_course,
        'last_date' : last_date
    }
    return render_to_response ('course_state_form.html', templ_data)


def set_userfieldparam (request, user_id, field_id, value):
    user = User.objects.get (pk = int (user_id))
    field = CourseField.objects.get (pk = int (field_id))
    userfieldparam = UserFieldParam.objects.filter (user = user, field = field)

    if len (userfieldparam) == 0:
        UserFieldParam.objects.update_or_create (user = user, field = field, value = value)
    else:
        cur_value = u';'.join ([userfieldparam [0].value, value]) if userfieldparam [0].value is not None else value
        userfieldparam.update (value = cur_value)
    return render_to_response ('empty.html')


def clear_userfieldparam (request, user_id, field_id):
    user = User.objects.get (pk = int (user_id))
    field = CourseField.objects.get (pk = int (field_id))
    userfieldparam = UserFieldParam.objects.filter (user = user, field = field)

    if len (userfieldparam) == 0:
        UserFieldParam.objects.update_or_create (user = user, field = field)
    else:
        userfieldparam.update (value = None)
    return render_to_response ('empty.html')


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


def get_report (request, course_id, user_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))

    empty_field = CourseField.objects.filter (userfieldparam__isnull = True, in_report = True)
    for field in empty_field:
        UserFieldParam.objects.update_or_create (user = user, field = field)

    uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)

    uallowance.report = 1

    uallowance.save()
    return render_to_response ('empty.html')


def check_workplace (request, course_id, user_id, standtask_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))
    standtask = Standtask.objects.get (pk = int (standtask_id))

    standtask_states = Standtask_state.objects.filter (user_id = user, standtask_id = standtask)
    for standtask_state in standtask_states:
        if standtask_state.complete:
            uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)
            uallowance.course_start = 1
            uallowance.save ()
        return JsonResponse ({'Complete' : standtask_state.complete, 'Error' : standtask_state.error})


def start_workplace (request, course_id, user_id, standtask_id):
    course = Course.objects.get (pk = int (course_id))
    user = User.objects.get (pk = int (user_id))
    standtask = Standtask.objects.get (pk = int (standtask_id))

    standtask_states = Standtask_state.objects.filter (user_id = user, standtask_id = standtask)
    for standtask_state in standtask_states:
        standtask_state.delete ()

    Standtask_state.objects.update_or_create (user_id = user, standtask_id = standtask, activate = True, complete = False, error = False)

    uallowance, _ = UserAllowance.objects.update_or_create (user = user, course = course)
    uallowance.course_start = 0
    uallowance.save()
    return render_to_response ('empty.html')
