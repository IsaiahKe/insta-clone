from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    name= models.CharField(max_length=20)
    user=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='images')
    caption=models.TextField(max_length=254)
    image=CloudinaryField('image')
    likes=models.IntegerField(default=0)
    def __str__(self):
        return self.user
    def save_user(self):
        self.save()
    @classmethod
    def posts(cls):
        posts=cls.objects.all()
        return posts
    
        
class Profile(models.Model):
    bio=models.TextField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    name=models.CharField(max_length=20,blank=True)
    photo=CloudinaryField('image')
    
    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
	    instance.profile.save()
    def __str__(self):
        return self.name
class Follow(models.Model):
    followed=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='followers'),
    following=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='following')
    
    
    def __str__(self):
        return f'{self.follower} Follower'
    
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='comment')
    photo = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comment')

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f'{self.user.name} Post'
    def savecomment(self):
        self.save()
    