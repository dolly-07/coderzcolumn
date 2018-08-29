from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'tutorials'

urlpatterns = [
    url('', views.tutorials_home, name='tutorials_home'),
    #url(r'^about/')
]