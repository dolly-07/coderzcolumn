from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'about'

urlpatterns = [
    url('', views.about, name='about')
]