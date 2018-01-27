# coding: utf-8

import json

from user.models import User


def set_point_by_job(user, point_dic):
    _RATIO_JOB = 0.5
    _JOB_SALES = 1
    _JOB_OFFICE = 2
    _JOB_RESEARCH = 3
    _JOB_PROFESSIONAL = 4
    _JOB_BUSINESS = 5
    _JOB_ETC = 6

    job = user.job

    if job == _JOB_SALES :
        point_dic['A'] += 20 * _RATIO_JOB
        point_dic['B'] += 10 * _RATIO_JOB
        point_dic['C'] += 40 * _RATIO_JOB
        point_dic['D'] += 20 * _RATIO_JOB
        point_dic['E'] += 10 * _RATIO_JOB
    elif job == _JOB_OFFICE:
        point_dic['A'] += 40 * _RATIO_JOB
        point_dic['B'] += 20 * _RATIO_JOB
        point_dic['C'] += 20 * _RATIO_JOB
        point_dic['D'] += 10 * _RATIO_JOB
        point_dic['E'] += 10 * _RATIO_JOB
    elif job == _JOB_RESEARCH:
        point_dic['A'] += 40 * _RATIO_JOB
        point_dic['B'] += 30 * _RATIO_JOB
        point_dic['C'] += 30 * _RATIO_JOB
        point_dic['D'] += 0 * _RATIO_JOB
        point_dic['E'] += 0 * _RATIO_JOB
    elif job == _JOB_PROFESSIONAL:
        point_dic['A'] += 30 * _RATIO_JOB
        point_dic['B'] += 40 * _RATIO_JOB
        point_dic['C'] += 20 * _RATIO_JOB
        point_dic['D'] += 10 * _RATIO_JOB
        point_dic['E'] += 0 * _RATIO_JOB
    elif job == _JOB_BUSINESS:
        point_dic['A'] += 20 * _RATIO_JOB
        point_dic['B'] += 40 * _RATIO_JOB
        point_dic['C'] += 20 * _RATIO_JOB
        point_dic['D'] += 20 * _RATIO_JOB
        point_dic['E'] += 0 * _RATIO_JOB
    return point_dic



def set_point_by_hobby_common(user, point_dic):
    _RATIO_HOBBY = 0.08
    _HOBBY_TOGETHER = 1
    _HOBBY_ALONE = 2
    hobby = user.hobby
    if hobby == _HOBBY_TOGETHER:
        point_dic['A'] += 30 * _RATIO_HOBBY
        point_dic['B'] += 20 * _RATIO_HOBBY
        point_dic['C'] += 30 * _RATIO_HOBBY
        point_dic['D'] += 10 * _RATIO_HOBBY
        point_dic['E'] += 10 * _RATIO_HOBBY
    elif hobby == _HOBBY_ALONE:
        point_dic['A'] += 30 * _RATIO_HOBBY
        point_dic['B'] += 50 * _RATIO_HOBBY
        point_dic['C'] += 20 * _RATIO_HOBBY
        point_dic['D'] += 0 * _RATIO_HOBBY
        point_dic['E'] += 0 * _RATIO_HOBBY
    return point_dic



def set_point_by_fashion_common(user, point_dic):
    _RATIO_FASHION = 0.15
    _FASHION_HIGH = 1
    _FASHION_CASUAL = 2
    _FASHION_PREPPY = 3
    _FASHION_SUIT = 4
    _FASHION_STREET = 5

    fashion = user.fashion

    if fashion == _FASHION_HIGH:
        point_dic['A'] += 30 * _RATIO_FASHION
        point_dic['B'] += 20 * _RATIO_FASHION
        point_dic['C'] += 40 * _RATIO_FASHION
        point_dic['D'] += 10 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_CASUAL:
        point_dic['A'] += 40 * _RATIO_FASHION
        point_dic['B'] += 30 * _RATIO_FASHION
        point_dic['C'] += 30 * _RATIO_FASHION
        point_dic['D'] += 0 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_PREPPY:
        point_dic['A'] += 20 * _RATIO_FASHION
        point_dic['B'] += 40 * _RATIO_FASHION
        point_dic['C'] += 20 * _RATIO_FASHION
        point_dic['D'] += 20 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_SUIT:
        point_dic['A'] += 30 * _RATIO_FASHION
        point_dic['B'] += 20 * _RATIO_FASHION
        point_dic['C'] += 40 * _RATIO_FASHION
        point_dic['D'] += 10 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_STREET:
        point_dic['A'] += 20 * _RATIO_FASHION
        point_dic['B'] += 40 * _RATIO_FASHION
        point_dic['C'] += 20 * _RATIO_FASHION
        point_dic['D'] += 20 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    return point_dic






def set_point_by_hobby_special(user, point_dic):
    _RATIO_HOBBY = 0.15
    _HOBBY_TOGETHER = 1
    _HOBBY_ALONE = 2
    hobby = user.hobby
    if hobby == _HOBBY_TOGETHER:
        point_dic['A'] += 30 * _RATIO_HOBBY
        point_dic['B'] += 20 * _RATIO_HOBBY
        point_dic['C'] += 30 * _RATIO_HOBBY
        point_dic['D'] += 10 * _RATIO_HOBBY
        point_dic['E'] += 10 * _RATIO_HOBBY
    elif hobby == _HOBBY_ALONE:
        point_dic['A'] += 30 * _RATIO_HOBBY
        point_dic['B'] += 50 * _RATIO_HOBBY
        point_dic['C'] += 20 * _RATIO_HOBBY
        point_dic['D'] += 0 * _RATIO_HOBBY
        point_dic['E'] += 0 * _RATIO_HOBBY
    return point_dic



def set_point_by_fashion_special(user, point_dic):
    _RATIO_FASHION = 0.15
    _FASHION_HIGH = 1
    _FASHION_CASUAL = 2
    _FASHION_PREPPY = 3
    _FASHION_SUIT = 4
    _FASHION_STREET = 5

    fashion = user.fashion

    if fashion == _FASHION_HIGH:
        point_dic['A'] += 5 * _RATIO_FASHION
        point_dic['B'] += 0 * _RATIO_FASHION
        point_dic['C'] += 5 * _RATIO_FASHION
        point_dic['D'] += 50 * _RATIO_FASHION
        point_dic['E'] += 40 * _RATIO_FASHION

    elif fashion == _FASHION_CASUAL:
        point_dic['A'] += 20 * _RATIO_FASHION
        point_dic['B'] += 0 * _RATIO_FASHION
        point_dic['C'] += 30 * _RATIO_FASHION
        point_dic['D'] += 50 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_PREPPY:
        point_dic['A'] += 30 * _RATIO_FASHION
        point_dic['B'] += 0 * _RATIO_FASHION
        point_dic['C'] += 30 * _RATIO_FASHION
        point_dic['D'] += 40 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_SUIT:
        point_dic['A'] += 30 * _RATIO_FASHION
        point_dic['B'] += 0 * _RATIO_FASHION
        point_dic['C'] += 10 * _RATIO_FASHION
        point_dic['D'] += 60 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    elif fashion == _FASHION_STREET:
        point_dic['A'] += 40 * _RATIO_FASHION
        point_dic['B'] += 0 * _RATIO_FASHION
        point_dic['C'] += 40 * _RATIO_FASHION
        point_dic['D'] += 20 * _RATIO_FASHION
        point_dic['E'] += 0 * _RATIO_FASHION

    return point_dic

def set_point_by_holiday(user, point_dic):
    _RATIO_HOLIDAY = 0.5
    _HOLIDAY_PARTY = 1
    _HOLIDAY_ALONE = 2
    _HOLIDAY_FRIEND = 3

    holiday = user.holiday

    if holiday == _HOLIDAY_PARTY:
        point_dic['A'] += 30 * _RATIO_HOLIDAY
        point_dic['B'] += 0 * _RATIO_HOLIDAY
        point_dic['C'] += 20 * _RATIO_HOLIDAY
        point_dic['D'] += 0 * _RATIO_HOLIDAY
        point_dic['E'] += 50 * _RATIO_HOLIDAY

    elif holiday == _HOLIDAY_ALONE:
        point_dic['A'] += 35 * _RATIO_HOLIDAY
        point_dic['B'] += 30 * _RATIO_HOLIDAY
        point_dic['C'] += 35 * _RATIO_HOLIDAY
        point_dic['D'] += 0 * _RATIO_HOLIDAY
        point_dic['E'] += 0 * _RATIO_HOLIDAY

    elif holiday == _HOLIDAY_FRIEND:
        point_dic['A'] += 30 * _RATIO_HOLIDAY
        point_dic['B'] += 5 * _RATIO_HOLIDAY
        point_dic['C'] += 40 * _RATIO_HOLIDAY
        point_dic['D'] += 20 * _RATIO_HOLIDAY
        point_dic['E'] += 5 * _RATIO_HOLIDAY

    return point_dic


def select_perfume_by_point(point_dic):
    PERFUME_CODE_A = "A"
    PERFUME_CODE_B = "B"
    PERFUME_CODE_C = "C"
    PERFUME_CODE_D = "D"
    PERFUME_CODE_E = "E"
    max_point = 0
    result_code = PERFUME_CODE_A
    for perfume_code, point in point_dic.items():    # for name, age in list.items():  (for Python 3.x)
        if max_point < point:
            result_code = perfume_code
            max_point = point
    return result_code

def validate_repeat(result_common, result_special):
    if result_common != result_special:
        return result_special
    else:
        if result_common == "A":
            return "D"
        elif result_common == "B":
            return "A"
        elif result_common == "C":
            return "D"
        elif result_common == "D":
            return "C"
        elif result_common == "E":
            return "C"
    return "A"
