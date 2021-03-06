"""coderzcolumn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.index, name='home'),
    path('logout/', views.lgout, name='logout'),
    path('ccadminpg/', admin.site.urls, name='admin'),

    path('howto/', views.index, name='howto'),
    path('researchpapers/', views.index, name='research'),
    path('blogs/', include('blogs.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('about/', include('about.urls')),
    path('login/', views.UserFormView.as_view(), name='login')


]
