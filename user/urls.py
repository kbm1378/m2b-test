# coding: utf-8


from django.conf.urls import url, include

from .api import *


urlpatterns = [
    url(r'^api/submit$', submit, name='submit'),
    url(r'^api/get_result$', get_result, name='get_result'),

]
