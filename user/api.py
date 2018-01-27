# coding: utf-8

from django.views.decorators.http import require_http_methods

import json
from django.http.request import QueryDict
from user.models import User
from perfume.models import UserPerfume, Perfume
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from perfume.helper import *

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


@csrf_exempt
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

    same_name_count = User.objects.filter(name=user.name).count()
    if same_name_count > 0:
        user.name_as_id = user.name + str(same_name_count+1)
    else:
        user.name_as_id = user.name
    user.save()

    point_dic_common = {'A':0,'B':0,'C':0,'D':0,'E':0}
    point_dic_special = {'A':0,'B':0,'C':0,'D':0,'E':0}

    point_dic_common = set_point_by_job(user, point_dic_common)
    point_dic_common = set_point_by_hobby_common(user, point_dic_common)
    point_dic_common = set_point_by_fashion_common(user, point_dic_common)
    result_common = select_perfume_by_point(point_dic_common)
    point_dic_special = set_point_by_holiday(user, point_dic_special)
    point_dic_special = set_point_by_hobby_special(user, point_dic_special)
    point_dic_special = set_point_by_fashion_special(user, point_dic_special)
    result_special = select_perfume_by_point(point_dic_special)
    result_special = validate_repeat(result_common, result_special)

    perfume_common = Perfume.objects.get(code=result_common)
    perfume_special =  Perfume.objects.get(code=result_special)
    _RECOMMEND_TYPE_COMMON = 1
    _RECOMMEND_TYPE_SPECIAL = 2
    user_perfume_common = UserPerfume.objects.create(user = user,
                                                     perfume = perfume_common,
                                                     recommend_type = _RECOMMEND_TYPE_COMMON)
    user_perfume_common.reason_text = ""
    user_perfume_common.save()

    user_perfume_special = UserPerfume.objects.create(user = user,
                                                     perfume = perfume_special,
                                                     recommend_type = _RECOMMEND_TYPE_SPECIAL)
    user_perfume_special.reason_text = ""
    user_perfume_special.save()


    data['page_id'] = user.name_as_id
    data['result'] = 'success'
    return JsonResponse(data)


@require_http_methods(["GET"])
def get_result(request):
    data = {'result': 'fail'}
    request = body_to_querydict(request)
    name_as_id = request.GET.get('name_as_id')
    users = User.objects.filter(name_as_id=name_as_id)

    if not users:
        data = {
                'result': 'fail',
                'error': 'User does not exist.'
            }
        return data, 404

    user = users.first()

    _RECOMMEND_TYPE_COMMON = 1
    _RECOMMEND_TYPE_SPECIAL = 2

    user_perfumes_common = UserPerfume.objects.filter(user = user,
                                                     recommend_type = _RECOMMEND_TYPE_COMMON)
    user_perfumes_special = UserPerfume.objects.filter(user = user,
                                                     recommend_type = _RECOMMEND_TYPE_SPECIAL)

    if not user_perfumes_common or not user_perfumes_special:
        data = {
                'result': 'fail',
                'error': 'UserPerfumes does not exist.'
            }
        return data, 404

    user_perfume_common = user_perfumes_common.first()
    user_perfume_special = user_perfumes_special.first()

    data['name'] = user.name
    data['perfume_common'] = user_perfume_common.perfume.code
    data['perfume_special'] = user_perfume_special.perfume.code
    data['perfume_common_reason_text'] = user_perfume_common.reason_text
    data['perfume_special_reason_text'] = user_perfume_special.reason_text
    data['result'] = 'success'
    return JsonResponse(data)
