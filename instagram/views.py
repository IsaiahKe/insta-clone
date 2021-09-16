from .models import Post
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    
    title="Instagram"
    posts=Post.posts()
    users= User.objects.exclude(id=request.user.id)
    return render(request, 'index.html',{'title':title,'users':users,"posts":posts})

@login_required(login_url='/accounts/login')
def createpost(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('index')      
    form=PostForm()
    return render(request,'post.html',{"postform":form})
