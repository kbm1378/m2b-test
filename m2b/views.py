# coding: utf-8

from django.shortcuts import render



def rendering_to_quiz(request):

    return render(request, 'quiz.html')
