# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blogs
from django.template import loader
# Create your views here.
from .forms import UserForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, user_logged_in, user_logged_out, user_login_failed, get_user
from django.views.generic import View


def index(request):
    msg = '<h1>Home Page</h1>'
    return HttpResponse(msg)


def blogs_home(request):
    #msg = '<h1>Blogs Home Page</h1>'
    blogs = Blogs.objects.all()
    template = loader.get_template('blogs/index.html')
    context = {'blogs': blogs}
    return HttpResponse(template.render(context, request))


def display_blog(request, category, blog_id):
    try:
        blog = Blogs.objects.get(pk=blog_id)
    except Blogs.DoesNotExist:
        return Http404('<h1>Blog does not exist</h1>')
    msg = '<h1>Blog Category : %s & Blog Id : %s</h1>' % (category, blog_id)
    return HttpResponse(msg)


class UserFormView(View):
    form_class = UserForm
    template_name = 'login.html'

    def get(self, request):
        pass

    def post(self, request):
        pass