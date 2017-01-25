from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#Request and Response things are the view

def post_create(request):
	return HttpResponse("<h1>Hello</h1>")

def post_detail(request):
	return HttpResponse("<h1>Hello</h1>")

def post_list(request):
	return HttpResponse("<h1>Hello</h1>")

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")

def post_home(request):
	return HttpResponse("<h1>Hello</h1>")