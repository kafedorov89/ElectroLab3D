# -*- coding: utf-8 -*-
"""electrolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from main import views


urlpatterns = [
    # Studenr urls
    url (r'^$', views.LoginFormView.as_view ()),
    url (r'^admin/', include (admin.site.urls)),
    url (r'^register/$', views.RegisterFormView.as_view ()),
    url (r'^login/$', views.LoginFormView.as_view ()),
    url (r'^logout/$', views.LogoutView.as_view ()),
    url (r'^main_menu/$', views.main_menu),
    url (r'^timetable/$', views.timetable),
    url (r'^method/([0-9]*)/$', views.method),
    url (r'^input_control/([0-9]*)/([0-9]*)/$', views.input_control),
    url (r'^workplace_construct/([0-9]*)/$', views.workplace_construct),
    url (r'^course/([0-9]*)/$', views.course),
    url (r'^report/([0-9]*)/$', views.report),
    url (r'^media_course/$', views.media_course),

    # Student service urls
    url (r'^load_answer/([0-9]*)/([0-9]*)/([0-9]*)/$', views.load_answer),
    url (r'^check_answer/([0-9]*)/([0-9]*)/$', views.check_answer),
    url (r'^check_workplace/([0-9]*)/([0-9]*)/([0-9]*)/$', views.check_workplace),
    url (r'^start_workplace/([0-9]*)/([0-9]*)/([0-9]*)/$', views.start_workplace),
    url (r'^set_userfieldparam/([0-9]*)/([0-9]*)/(.*)/$', views.set_userfieldparam),
    url (r'^clear_userfieldparam/([0-9]*)/([0-9]*)/$', views.clear_userfieldparam),
    url (r'^get_report/([0-9]*)/([0-9]*)/$', views.get_report),

    # Teacher urls
    url (r'^teacher_main_menu/$', views.teacher_main_menu),
    url (r'^timetable_editor/$', views.timetable_editor),
    url (r'^course_state_form/([a-z]*)/$', views.course_state_form),
    url (r'^course_state_form/([a-z]*)/([0-9]*)/$', views.course_state_form),
    url (r'^course_view/$', views.course_view),
    url (r'^teacher_report/$', views.teacher_report),
    url (r'^course_usg_view/$', views.course_usg_view),
    url (r'^teacher_usg_report/$', views.teacher_usg_report),

    # Teacher service urls
    url (r'^course_state_cng/([0-9]*)/([0-9]*)/([0-9]*)/(\d{2}.\d{2}.\d{4})/([0-9]*)/$', views.course_state_cng),
    url (r'^course_state_add/([0-9]*)/([0-9]*)/(\d{2}.\d{2}.\d{4})/([0-9]*)/$', views.course_state_add),
    url (r'^course_state_del/([0-9]*)/$', views.course_state_del),
]
