from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from register import views

urlpatterns = [
    re_path(r'^register/$', views.RegisterList.as_view()),
    re_path(r'^teams/$', views.TeamsList.as_view()),
]
