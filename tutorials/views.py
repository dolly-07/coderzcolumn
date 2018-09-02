# -*- coding: utf-8 -*-
from django.shortcuts import render


def tutorials_home(request):
    return render(request, 'tutorials/tutorials_home.html')
