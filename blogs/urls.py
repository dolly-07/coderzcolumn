from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^about/')
    url(r'^(?P<category>[a-zA-Z]+)/(?P<blog_id>[0-9]+)$', views.display_blog, name='display_blog')
]