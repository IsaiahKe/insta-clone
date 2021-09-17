from django import forms
from django.db.models.expressions import Col
from django.forms import widgets
from .models import Comment, Post, Profile, User
from instagram import models
#create forms for the application
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        exclude=['followers','following','rdate']
        widgets={
            'password':forms.PasswordInput(),
            'confirm_password':forms.PasswordInput()
        }
        
    
  
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        exclude=['first_name','surname','rdate','followers','following','confirm_password']
        widgets={
            'password':forms.PasswordInput(),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','name']
        widgets={
            'caption':forms.Textarea(),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user_id','user','name']
        widgets={
            'bio':forms.Textarea(),
            'image':forms.ImageField()
        }
class UpdateUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name')
