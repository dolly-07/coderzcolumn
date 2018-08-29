from django.conf.urls import url
from . import views
from django.urls import path

app_name='blogs'

urlpatterns = [

    path('', views.blogs_home, name='blogs_home'),
    path('<str:category>/<int:blog_id>', views.display_blog, name='display_blog'),
]