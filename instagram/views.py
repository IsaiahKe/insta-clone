from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    title="User Registration"
    
    form=RegisterForm()
    if form.is_valid():
        if request.method=='POST':
            
    else:
        HttpResponseRedirect('register')
    return render(request,'django_registration/registration_form.html',{"title":title,"form":form})

def login(request):
    title="User Login"
    form=LoginForm()
    if form.is_valid():
        print('good')
    else:
        HttpResponseRedirect("login")
    return render(request,'django_registration/registration_complete.html',{"title":title,"form":form})

@login_required(login_url='/django_registration/login')
def index(request):
    
    title="Instagram"
    return render(request, 'index.html',{'title':title})
