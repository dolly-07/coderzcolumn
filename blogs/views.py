# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from .models import Blogs, Author
from .forms import UserForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, get_user
from django.views.generic import View
from .forms import UserForm


def index(request):
    username = get_user(request)
    username = username if username.is_authenticated else None
    return render(request, 'blogs/home.html', {'username': username})


def lgout(request):
    logout(request)
    print('User Logged out')
    return render(request, 'blogs/home.html', {'username': None})


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
    template_name = 'blogs/login.html'

    ## Displays Blank form
    def get(self, request):
        #print('Get')
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'error_message': None})

    ## Process form registration
    def post(self, request):
        print(request.POST)
        if 'lpwd' in request.POST:

            form = self.form_class({
                'username': request.POST['user'],
                'password': request.POST['lpwd'],
            })
            if not request.POST['user'] or  ' ' in request.POST['user']:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Login failed. Please provide proper username.'})
            if not request.POST['lpwd']:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Login failed. Please provide password.'})

            username = request.POST['user'].strip()
            password = request.POST['lpwd'].strip()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    error_message = 'User login failed. User Inactive.'
            else:
                error_message = 'User login failed. Invalid username/password'
        else:
            form = self.form_class({
                                    'username': request.POST['nick'],
                                    'email': request.POST['remail'],
                                    'password': request.POST['rpwd'],
                                    })
            if not request.POST['nick'] or  ' ' in request.POST['nick']:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Registration failed. Please provide proper username.'})
            if not request.POST['rpwd']:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Registration failed. Please provide password.'})
            if not request.POST['remail']:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Registration failed. Please provide email.'})
            if 'terms' not in request.POST:
                return render(request, self.template_name,
                       {'form': form, 'error_message': 'Registration failed. Please accept terms & conditions'})

            if form.is_valid():
                print('Inside Form IF')
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user.set_password(password)
                user.save()
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        author = Author(nick_name=request.POST['nick'],
                                        email=request.POST['remail'],
                                        intro=request.POST['intro'],
                                        about=request.POST['about'])
                        author.save()
                        login(request, user)
                        return redirect('home')
                    else:
                        error_message = 'User registration failed. User Inactive.'
                else:
                    error_message = 'User registration failed. Username/email address already exist'
            else:
                error_message = 'User registration failed. Username/email address already exist'

        return render(request, self.template_name, {'form': form, 'error_message' : error_message})












