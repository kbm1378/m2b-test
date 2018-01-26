# coding: utf-8

from django.db import models

# Create your models here.
from user.models import User

class Perfume(models.Model):
    code = models.CharField(max_length=50, verbose_name='향수 코드 (A, B, C, D, E)')
    tagtext = models.CharField(max_length=50, verbose_name='향수 설명 태그 텍스트')
    imageurl_1_common = models.URLField(max_length=500, null=True, blank=True, verbose_name='Common일 경우 1번째 이미지 url')
    imageurl_2_common = models.URLField(max_length=500, null=True, blank=True, verbose_name='Common일 경우 2번째 이미지 url')
    imageurl_3_common = models.URLField(max_length=500, null=True, blank=True, verbose_name='Common일 경우 3번째 이미지 url')
    imageurl_1_special = models.URLField(max_length=500, null=True, blank=True, verbose_name='Special일 경우 1번째 이미지 url')
    imageurl_2_special = models.URLField(max_length=500, null=True, blank=True, verbose_name='Special일 경우 2번째 이미지 url')
    imageurl_3_special = models.URLField(max_length=500, null=True, blank=True, verbose_name='Special일 경우 3번째 이미지 url')

class PerfumeComment(models.Model):
    perfume =  models.ForeignKey(Perfume, on_delete=models.CASCADE, verbose_name='추천 향수')
    reason_paragraph = models.TextField(verbose_name='향수 추천 문구') # ~에 맞는 달콤하면서도 깔끔한 첫인상을 주는 Saffron과 Mayrose가 있는 향입니다.

class UserPerfume(models.Model):
    _RECOMMEND_TYPE = (
        (1, 'COMMON'),
        (2, 'SPECIAL'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='유저') #유저
    perfume =  models.ForeignKey(Perfume, on_delete=models.CASCADE, verbose_name='추천 향수')
    recommend_type  = models.IntegerField(choices=_RECOMMEND_TYPE, blank=True, null=True, verbose_name='추천 타입(Special or Common)')
    reason_text = models.TextField(verbose_name='추천 이유')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='최종 수정일')
