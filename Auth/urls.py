from django.urls import path
from django.conf.urls import url
from Auth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^oauth/$', views.oauth, name='oauth'),
    url(r'^home/$', views.home, name='home'),
]
