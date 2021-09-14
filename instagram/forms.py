from django import forms
from django.forms import widgets
from .models import User
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