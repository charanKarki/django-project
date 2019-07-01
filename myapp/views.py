from django.shortcuts import render
from .models import post
from .form import userForm

# Create your views here.


def home(request):
    return  render(request,'home.html')

def about(request):
    return render(request,"about.html")

def contectUs(request):
    return render(request,"contectUs.html")

def login(request):
    return render(request,'login.html',{'form':userForm})

def signup(request):
    return render(request,'signup.html',{'form':userForm})

def blog(request):
    posts = post.objects.all()
    return render(request,'blog.html',{
        'posts':posts
    })



