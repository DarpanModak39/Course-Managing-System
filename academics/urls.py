from django.contrib import admin
from django.urls import path
from academics import views

urlpatterns = [
    path('login', views.loginuser,name='loginuser'),
    path('faculty', views.faculty,name='faculty'),
    path('hod', views.hod,name='hod'),
    path('logout',views.logoutuser,name='logoutuser'),
    path('addcoursecontent', views.addcoursecontent,name='addcoursecontent'),
    path('viewcourse', views.viewcourse,name='viewcourse'),
    path('addcourse', views.addcourse,name='addcourse'),
    path('modifycourse', views.modifycourse,name='modifycourse'),
    path('deletecourse', views.deletecourse,name='deletecourse'),
]