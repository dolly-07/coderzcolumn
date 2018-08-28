# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def about_home(request):
    msg = '<h1>Blogs Home Page</h1>'
    return HttpResponse(msg)
