from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 	url(r'^$', views.home),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', auth_views.login), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),

    url(r'^fypusRequest/$', views.fypusRequest),
    url(r'^index/$', views.index),
    url(r'^joinRequest/$', views.joinRequest),
    url(r'^profile/$', views.profile),
    url(r'^requestRecieved/$', views.requestRecieved),
    url(r'^yourSavings/$', views.yourSavings),
]
