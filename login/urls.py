from django.urls import path
from .import views
urlpatterns = [
  
   path("login",views.login,name='login'),
   path("registration_user",views.user_registration,name='user_registration'),
   path("registration_manager",views.manager_registration,name='manager_registration')
]