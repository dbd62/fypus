from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
 	url(r'^$', views.home),
    url(r'^logout/$', views.logout_page),
    url(r'^accounts/login/$', auth_views.login), # If user is not login it will redirect to login page
    url(r'^register/$', views.register),
    url(r'^registeration/register/$', views.register),
    url(r'^home/$', views.home),
    url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^profile/$', views.profile),
    url(r'^base/$', views.base),
    url(r'^fypusRequestYou/$', views.fypusRequestYou),
    url(r'^index/$', views.index),
    url(r'^home/$', views.home),
    url(r'^join/$', views.join),
    url(r'^login/$', views.login),
    url(r'^profile/$', views.profile),
    url(r'^RecruitOthers/$', views.recruitOthers),
    url(r'^RequestRecieved/$', views.requestRecieved),
    url(r'^RequestToJoin/$', views.requestToJoin),
    url(r'^YourSavings/$', views.yourSavings),
]
