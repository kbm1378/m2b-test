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


def generate_common_reason_text(user, user_perfume_common):
    job = "<strong>" + user.get_job_display() + "</strong>"
    fashion = "<strong>" + user.get_fashion_display() + "</strong>"
    introversion = "<strong>" + user.get_introversion_display() + "</strong>"
    perfume_code = user_perfume_common.perfume.code
    reason_text = ""

    if perfume_code == "A":
        reason_text = """탑노트의 시트러스계열인 상큼한 버가못과 레몬이 당신의 기분을 전환시켜줍니다.
        플로럴계열의 제라늄이 """ + job + """공간에서 부드럽고 여유있는 당신을 표현하고,
        우디계열의 샌달우드와 시더우드가""" + fashion + """을 즐겨입는 감각적인 모습을 나타냅니다. 플로럴계열과 우디계열이 중심을 잡고 있는 이 향은 부드러우면서 밝은 분위기를 지닌 당신을 나타냅니다."""

    elif perfume_code == "B":
        reason_text = """버가못의 시트러스함이 당신의""" + introversion + """의 분위기를 친숙하게 만들어주고, 상쾌한 스파이시 느낌의 카다몬의 독특함이""" + fashion + """
        을 선호하는 당신을 표현합니다. 허브를 닮은 장미 향, Geranium이 """ + job + """에 종사하는 당신에게 밝은 분위기를 심어주고, 핑크페퍼의 스파이시함이 득별한 느낌을 줍니다.
        Tonkabean의 발삼한 따뜻한 느낌과 Vetiver가 만나 독특하지만 데일리로 사용하기 좋습니다."""

    elif perfume_code == "C":
        reason_text = """탑노트의 플로럴계열인 샤프란과 메이로즈가 """ + job + """에서 친근감있는 당신을 달콤하게 드러냅니다.
        플로럴계열의 로즈페탈과 스파이시계열의 블랙페퍼가 독특하게 어우러져 """ + fashion + """을 즐겨입는 당신의 젠틀함을 나타내고, 우디계열의 샌달우드, 파츌리와 파우더리계열의 앰버가 어우러져 신중하면서도 여유있는 당신을 표현합니다.
        플로럴 계열이 중심을 이루고 있는 이 향은 부드러운 모습이 매력적인 당신을 표현합니다."""

    elif perfume_code == "D":
        reason_text = """탑노트의 시트러스 계열인 버가못과 레몬이 당신의""" + introversion + """인 분위기를 친숙하게 다가오도록 하고, 상쾌한 솔잎 향기가 """ + fashion + """
        을 즐겨입는 당신과 어울리며 파우더리한 Woody는 """ + job + """에 종사하는 당신에게 어울리는 신중함을 표현합니다."""

    return reason_text





def generate_special_reason_text(user, user_perfume_special):
    job = "<strong>" + user.get_job_display() + "</strong>"
    fashion = "<strong>" + user.get_fashion_display() + "</strong>"
    introversion = "<strong>" + user.get_introversion_display() + "</strong>"
    holiday = "<strong>" + user.get_holiday_display() + "</strong>"
    hobby = "<strong>" + user.get_hobby_display() + "</strong>"
    perfume_code = user_perfume_special.perfume.code
    reason_text = ""

    if perfume_code == "A":
        reason_text = """탑노트의 시트러스 계열인 상큼한 버가못과 레몬이 """ + holiday + """를 즐기는 당신의 기분을 전환시켜,
        허브를 닮은 장미향의 제라늄이 당신의 매력을 더욱 자신감 있게 표현합니다.
        우디계열의 샌달우드와 시더우드가 """ + hobby + """를 즐기는 당신의 세련된 모습을 드러냅니다.
        플로럴계열과 우디계열이 중심을 잡고 있는 이 향은 도회적인 당신의 중후한 매력을 부드럽게 부각시킵니다."""


    elif perfume_code == "C":
        reason_text = """탑노트의 플로럴계열인 샤프란과 메이로즈가 """ + holiday + """를 즐기는 당신을 감미롭게 나타내기 시작하여,
        스파이시계열의 블랙페퍼와 플로럴계열의 로즈페탈이 어우러져 당신의 강렬한 열정을 드러냅니다.
        우디계열의 샌달우드, 파츌리와 오리엔탈 계열의 앰버가 조화되어 """ + hobby + """을 즐기는 당신에게 은근한 섹시함을 느끼게 합니다.
        플로럴 계열이 중심을 이루고 있는 이 향은 매혹적인 당신의 모습을 관능적으로 표현합니다."""


    elif perfume_code == "D":
        reason_text = """신선한 시트러스 Bergamot, Lemon으로 시작해 친숙하게 다가오도록 하고 상쾌하고 차분한 솔잎 향기가 """ + hobby + """의 성격과 어울리며
        파우더리한 Woody가 """ + holiday + """에 어울리는 당신을 더욱 센스있게 표현해 줄 것입니다."""

    elif perfume_code == "E":
        reason_text =  holiday + """에 어울리는 바디는 Tuberose로 이성을 유혹하는 치명적이고 “위험한 관계”라는 꽃말과 같이 관능적이고 깊이 있는 플로럴함이 """ + hobby + """를 즐기는 당신에게 어울리는
        YlangYlang을 만나 고급스러운 풍부함을 더해주고 잔향이 부드럽고 포근하게 느껴집니다."""

    return reason_text
