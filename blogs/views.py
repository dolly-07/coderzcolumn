# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from .models import Blogs
from django.template import loader
from .forms import UserForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, user_logged_in, user_logged_out, user_login_failed, get_user
from django.views.generic import View


def index(request):
    return render(request, 'blogs/home.html')

def login(request):
    return render(request, 'blogs/login.html')

def blogs_home(request):
    blogs = Blogs.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs_home.html', context)


def display_blog(request, category, blog_id):
    try:
        blog = Blogs.objects.get(pk=blog_id)
    except Blogs.DoesNotExist:
        return Http404('<h1>Blog does not exist</h1>')
    context = {'blog': blog}
    return render(request, 'blogs/blog_display.html', context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'login.html'

    def get(self, request):
        pass

    def post(self, request):
        pass