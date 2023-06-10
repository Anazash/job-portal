from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('products',views.products,name='products'),
    path('resources',views.resources,name='resources'),
    path('helpcenter',views.helpcenter,name='helpcenter'),
    path('findjobs',views.findjobs,name='findjobs'),
    path('postjobs',views.postjobs,name='postjobs'),
    path('showjob',views.showjob,name='showjob'),
    path('messages',views.messages,name='messages'),
    path('profile',views.profile,name='profile'),
    path('seeprofile',views.seeprofile,name='seeprofile'),

]