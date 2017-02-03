from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.
#Request and Response things are the view

def post_list(request):
	'''if request.user.is_authenticated():
		context = {
			"title" : "My user list"
		}
	else:
		context = {
			"title" : "List"
		}'''

	queryset = Post.objects.all()
	context = {
			"object_list": queryset, 
			"title" : "List",
		}

	return render (request, "index.html", context)
	#return HttpResponse("<h1>Hello</h1>")

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
	context = {
		"form" : form,
	}
	return render (request, "post_form.html", context)

def post_detail(request, id):
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title" : instance.title,
		"instance" : instance,

	}
	return render (request, "post_detail.html", context)

def post_update(request):
	return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
	return HttpResponse("<h1>Hello</h1>")
