from django.urls import path
from django.conf.urls import url
from Auth import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^home/$',views.home,name='home'),
]