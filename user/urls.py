# coding: utf-8


from django.conf.urls import url, include

from .api import *


urlpatterns = [
    url(r'^submit$', submit, name='submit'),

]
