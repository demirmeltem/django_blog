from django.conf.urls import url
from django.contrib import admin
#from posts.views import post_home
from . views import (	post_list,
					post_create,
					post_detail,
					post_update,
					post_delete,
)

urlpatterns = [
    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'), 
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete ),
   
]

