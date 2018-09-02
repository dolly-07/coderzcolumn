# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import datetime


class Author(models.Model):

    author_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='AUTHOR_ID')
    nick_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    intro = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    can_blog = models.BooleanField(default=False)

    def __str__(self):
        return self.nick_name


class Blogs(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    blog_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='BLOG_ID')
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    time_to_read = models.IntegerField(default=0)
    tags = models.CharField(max_length=500)

    def __str__(self):
        return self.title





