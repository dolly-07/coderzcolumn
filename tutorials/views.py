# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def tutorials_home(request):
    msg = '<h1>Tutorials Home Page</h1>'
    return HttpResponse(msg)
