from django.urls import path
from .import views

urlpatterns = [

   path("login",views.login,name='manager_home'),
   path("manager_registration",views.manager_register,name='registermanager'),
   path("user_registration",views.user_register,name='registeruser')
   
]