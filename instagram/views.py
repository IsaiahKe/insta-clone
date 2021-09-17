from django.conf.urls import url
from .models import Comment, Post, Profile
from django.shortcuts import render,redirect
from .forms import PostForm, ProfileForm,UpdateUserForm
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
@login_required(login_url="/accounts/login")
def comment(request,id):
   if request.method=="POST": 
    me=request.POST.get("comment")
    comment=Comment.objects.create(comment=me,photo_id=id,user=request.user.profile,)
    comment
        

    return redirect('index')

@login_required(login_url='/accounts/login')
def showprofile(request,id):
    currentuser=User.objects.get(pk=id)
    profile=Profile.objects.filter(user_id=id)
    image=Post.objects.filter(user_id=id)
    print(image)
    return render(request,'profile.html',{"images":image,"currentuser":currentuser,'profile':profile})
@login_required(login_url="/accounts/login")
def updateprofile(request,id):
    if request.method=="POST":
        form=ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        form2=UpdateUserForm()
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            print(form,form2)
            redirect('index')
    else:
       form=ProfileForm()
       form2=UpdateUserForm()
    return render(request,'updateprofile.html',{'form':form,"form2":form2})

@login_required(login_url="/accounts/login/")
def showcomments(request,id):
    comments=Comment.objects.filter(post_id=id)
    post=Post.objects.get(pk=id)
    return render(request,"comment.html",{"comments":comments,"post":post})
