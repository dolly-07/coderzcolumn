# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    intro = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    password = models.CharField(max_length=100)

class Blogs(models.Model):
    blog_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='BLOG_ID')
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    #author = models.CharField(max_length=50)
    author_id = models.ForeignKey(Author, max_length=50, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    time_to_read = models.TimeField()
    tags = models.CharField(max_length=500)

