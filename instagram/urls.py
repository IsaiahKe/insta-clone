from . import views
from django.conf.urls import url,include
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url('^$',views.index,name='index'),
    url('logout/$', LogoutView, {"next_page": '/'}),
    url('tinymce/',include('tinymce.urls')),
    url('^createpost/',views.createpost,name='createpost'),
    url('^comment/(\d)/',views.comment,name="comment"),
    url('^profile/(\d)/',views.showprofile,name="profile"),
    url('^profile/update/(\d)/',views.updateprofile,name="updateprofile"),
    url('^(\d)/comment/',views.showcomments,name="comments")
    
]