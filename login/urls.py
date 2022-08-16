from django.urls import path
from .import views

urlpatterns = [

   path("login_page",views.login,name='login'),
   path("manager_registration",views.register_manager,name='manager_register'),
   path("user_registration",views.register_user,name='user_register')
   
]