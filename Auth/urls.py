from django.urls import path
from django.conf.urls import url
from Auth import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]