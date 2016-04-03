# -*- encoding: UTF-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from models import Room
from main.models import Course, UserAllowance, UserCourseState



@csrf_exempt
def send (request):
    '''
    Expects the following POST parameters:
    chat_room_id
    message
    '''
    p = request.POST
    r = Room.objects.get (id = int (p ['chat_room_id']))

    current_user = request.user
    r.say (current_user, p ['message'])
    return HttpResponse ('')


@csrf_exempt
def sync (request):
    '''Return last message id

    EXPECTS the following POST parameters:
    id
    '''
    if request.method != 'POST':
        raise Http404
    post = request.POST

    if not post.get ('id', None):
        raise Http404

    r = Room.objects.get (id = post['id'])

    lmid = r.last_message_id ()

    return HttpResponse (jsonify ({'last_message_id':lmid}))

@csrf_exempt
def receive (request):
    '''
    Returned serialized data
    
    EXPECTS the following POST parameters:
    id
    offset
    
    This could be useful:
    @see: http://www.djangosnippets.org/snippets/622/
    '''
    if request.method != 'POST':
        raise Http404
    post = request.POST

    if not post.get ('id', None) or not post.get ('offset', None):
        raise Http404

    try:
        room_id = int (post ['id'])
    except:
        raise Http404

    try:
        offset = int (post ['offset'])
    except:
        offset = 0

    r = Room.objects.get (id = room_id)

    m = r.messages (offset)

    return HttpResponse (jsonify (m, ['id', 'author', 'message', 'type']))


@csrf_exempt
def join (request):
    '''
    Expects the following POST parameters:
    chat_room_id
    message
    '''
    p = request.POST
    r = Room.objects.get (id = int (p ['chat_room_id']))
    current_user = request.user
    r.join (current_user)
    return HttpResponse ('')


@csrf_exempt
def leave (request):
    '''
    Expects the following POST parameters:
    chat_room_id
    message
    '''
    p = request.POST
    r = Room.objects.get (id = int(p['chat_room_id']))
    current_user = request.user
    r.leave (current_user)
    return HttpResponse ('')


@login_required
def chat (request, course_id, user_id):

    course = Course.objects.get (pk = int (course_id))
    uallowance, _ = UserAllowance.objects.update_or_create (user = request.user, course = course)
    ucs = UserCourseState.objects.filter (user = user_id, course__id = course_id)
    r = Room.objects.get_or_create (ucs [0])

    templ_data = {
        'course' : True,
        'id': course_id,
        'number': course.name,
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'uallowance' : uallowance,
        'host' : request.get_host(),
        'user' : request.user,
        'js' : ['/media/js/mg/chat.js'],
        'chat_id' : r.pk
    }

    return render_to_response ('chat.html', templ_data, context_instance = RequestContext (request))


@login_required
def teacher_chat (request, course_id, user_id):

    ucs = UserCourseState.objects.filter (user = user_id, course__id = course_id)
    r = Room.objects.get_or_create (ucs [0])

    templ_data = {
        'date' : "{:%Y %m %d}".format (datetime.now()),
        'time' : "{:%H:%M}".format (datetime.now()),
        'js' : ['/media/js/mg/chat.js'],
        'chat_id' : r.pk
    }

    return render_to_response ('teacher_chat.html', templ_data, context_instance = RequestContext (request))


def jsonify (object, fields = None, to_dict = False):
    '''Simple convert model to json'''
    try:
        import json
    except:
        import django.utils.simplejson as json

    out = []
    if type (object) not in [dict, list, tuple] :
        for i in object:
            tmp = {}
            if fields:
                for field in fields:
                    tmp [field] = unicode (i.__getattribute__ (field))
            else:
                for attr, value in i.__dict__.iteritems ():
                    tmp [attr] = value
            out.append (tmp)
    else:
        out = object
    if to_dict:
        return out
    else:
        return json.dumps (out)
