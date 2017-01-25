from django.conf.urls import url
from django.contrib import admin
from posts.views import post_home

urlpatterns = [
    url(r'^$', post_home),
   
]

