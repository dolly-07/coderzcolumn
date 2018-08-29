# -*- coding: utf-8 -*-
from django.shortcuts import render
from blogs.models import Author


def about(request):
    authors = Author.objects.all()
    return render(request, 'about/about.html', {'authors': authors})
