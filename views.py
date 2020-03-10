from django.shortcuts import render,redirect
from . forms import shop,UserFilter
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Post


def printer(request):
    if request.method == "POST":
        form = shop(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = shop()
    return render(request,'test.html',{'form':form})

def delete(request,id):
    post_to_delete=Post.objects.get(id=id)
    post_to_delete.delete()
    x = Post.objects.all()
    return  render(request,'test2.html',{'all_items':x}) 

def search(request):
    user_list = Post.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'searcher.html', {'filter': user_filter})


def todoView(request):
	x = Post.objects.all()
	return  render(request,'test2.html',{'all_items':x}) 
