
from django.urls import path
from . import views

urlpatterns = [
     path('',views.signup,name='signup'),
     path('login',views.login,name='login'),
     path('logout',views.logout,name='logout'),
     path('home',views.home,name='home'),
     path('upload',views.upload,name='upload'),
     path('setting',views.setting,name='setting'),
      path('delete',views.delete,name='delete'),
      path('signup',views.signup,name='signup'),
]