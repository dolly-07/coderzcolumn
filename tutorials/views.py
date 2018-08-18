# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.

def index(request):
    msg = '<h1>Blogs Home Page</h1>'
    return HttpResponse()
