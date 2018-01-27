# coding: utf-8

from django.views.decorators.http import require_http_methods

import json
from django.http.request import QueryDict
from user.models import User
from django.http import JsonResponse

def body_to_querydict(request):
    if 'application/json' in request.META['CONTENT_TYPE']:
        data = json.loads(request.body.decode('utf-8'))
        q_data = QueryDict('', mutable=True)

        for key in data.keys():
            if isinstance(data[key], list):
                for x in data[key]:
                    q_data.update({key: x})
            else:
                q_data.update({key: data[key]})

        if request.method == 'GET':
            request.GET = q_data

        if request.method == 'POST':
            request.POST = q_data
        return request
    return request


@require_http_methods(["POST"])
def submit(request):
    data = {'result': 'fail'}
    request = body_to_querydict(request)

    user = User.objects.create()
    if request.POST.get('color'):
        user.color = int(request.POST.get('color'))
    if request.POST.get('job'):
        user.job = int(request.POST.get('job'))
    if request.POST.get('hobby'):
        user.hobby = int(request.POST.get('hobby'))
    if request.POST.get('food'):
        user.food = int(request.POST.get('food'))
    if request.POST.get('fashion'):
        user.fashion = int(request.POST.get('fashion'))
    if request.POST.get('introversion'):
        user.introversion = int(request.POST.get('introversion'))
    if request.POST.get('heat'):
        user.heat = int(request.POST.get('heat'))
    if request.POST.get('holiday'):
        user.holiday = int(request.POST.get('holiday'))
    if request.POST.get('my_perfume'):
        user.my_perfume = request.POST.get('my_perfume')
    if request.POST.get('gender'):
        user.gender = int(request.POST.get('gender'))
    if request.POST.get('age'):
        user.age = int(request.POST.get('age'))
    if request.POST.get('name'):
        user.name = request.POST.get('name')
    user.save()


    data['result'] = 'success'
    return JsonResponse(data)
