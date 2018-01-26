from django.db import models

# Create your models here.


class User(models.Model):


    _COLOR = (
        (1, '빨강'),
        (2, '노랑'),
        (3, '초록'),
        (4, '파랑'),
        (5, '검정'),
        (6, '흰색'),
    )

    _JOB = (
        (1, '영업직'),
        (2, '사무직'),
        (3, '연구직'),
        (4, '전문직'),
        (5, '사업가'),
        (6, '기타'),
    )

    _HOBBY = (
        (1, '사람들과 함께 하는 취미'),
        (2, '혼자서 하는 취미'),
    )

    _FOOD = (
        (1, '채식'),
        (2, '균형'),
        (3, '육식'),
    )

    _FASHION = (
        (1, '하이패션'),
        (2, '캐주얼'),
        (3, '프레피'),
        (4, '슈트'),
        (5, '스트릿'),
    )

    _INTROVERSION = (
        (1, '매우 외향적'),
        (2, '외향적'),
        (3, '보통'),
        (4, '내향적'),
        (5, '매우 내향적'),
    )

    _HEAT = (
        (1, '차가운 편'),
        (2, '보통'),
        (3, '뜨거운 편'),
    )

    _HOLIDAY = (
        (1, '클럽/파티'),
        (2, '혼자서 보내는 여유'),
        (3, '친구/연인과의 데이트'),
    )

    _CHANNEL = (
        (1, '지인추천'),
        (2, '페이스북'),
        (3, '인스타그램'),
        (4, '검색엔진 검색'),
        (5, '기타'),
    )

    _GENDER = (
        (1, '남자'),
        (2, '여자'),
    )


    color = models.IntegerField(choices=_COLOR, blank=True, null=True, verbose_name='좋아하는 색은?')
    job = models.IntegerField(choices=_JOB, blank=True, null=True, verbose_name='다니고 있는 직장은?')
    hobby = models.IntegerField(choices=_HOBBY, blank=True, null=True, verbose_name='가지고 있는 취미는?')
    food = models.IntegerField(choices=_FOOD, blank=True, null=True, verbose_name='좋아하는 음식의 분류는?')
    fashion = models.IntegerField(choices=_FASHION, blank=True, null=True, verbose_name='자주 입는 패션 스타일은?')
    introversion = models.IntegerField(choices=_INTROVERSION, blank=True, null=True, verbose_name='주로 나타나는 성격은?')
    heat = models.IntegerField(choices=_HEAT, blank=True, null=True, verbose_name='몸에 열이 나는 정도는?')
    holiday = models.IntegerField(choices=_HOLIDAY, blank=True, null=True, verbose_name='시간의 여유가 있을때 주로 무엇을?')
    my_perfume = models.TextField(verbose_name='현재 내가 가지고 있는 향수는?')

    channel = models.IntegerField(choices=_CHANNEL, blank=True, null=True, verbose_name='tobe를 알게 된 경로는?')
    name = models.CharField(max_length=50, verbose_name='이름')
    age = models.IntegerField(null=True, blank=True, verbose_name='나이')
    gender = models.IntegerField(choices=_GENDER, blank=True, null=True, verbose_name='성별')
    comment = models.TextField(verbose_name='기타 문의사항')
