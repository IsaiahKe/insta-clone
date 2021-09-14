from typing import BinaryIO
from django.db import models
from django.forms.widgets import PasswordInput
from django.utils import timezone
from django.db.models.fields import CharField
from tinymce.models import HTMLField
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=20)
    surname= models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=30,)
   
    rdate=models.DateField(default=timezone.now)
    followers=models.SmallIntegerField(default=0)
    following=models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.username
    def save_user(self):
        self.save()
        
class UserInfo(models.Model):
    bio=HTMLField()
    nickname=models.CharField(max_length=15)
    phone=models.IntegerField()
    profilephoto=models.ImageField()
    
    def __str__(self):
        self.nickname