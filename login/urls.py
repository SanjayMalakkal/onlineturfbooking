from django.urls import path
from .import views

urlpatterns = [

   path("",views.home,name='home'),
   path("login",views.login,name='log_in'),
   path("manager_registration",views.register_manager,name='manager_register'),
   path("user_registration",views.register_user,name='user_register')
   
]