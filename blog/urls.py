from django.urls import path, re_path
from blog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.number, name='contact'),
    path('books', views.contact, name='books'),
    path('name',views.get_name),
    path('allnames',views.names,name='allnames'),
    re_path(r'allnames/edit/(?P<edit_name>\d+)',views.edit_name,name='edit'),
    re_path(r'signup/$',views.signup),
    re_path(r'login/$',views.login),
    re_path(r'^post/new/$', views.create_post),
    path('allpost',views.all_post),


 ]


