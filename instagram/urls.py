from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^accounts/register$',views.register,name='register'),
    url(r'^accounts/login$',views.login,name='login'),
]
