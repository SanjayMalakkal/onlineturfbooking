from django.urls import path
from .import views
app_name = 'login'
urlpatterns = [

   path("",views.home,name='home'),
   path("userlogin",views.login,name='userlogin'),
   path("manager_registration",views.register_manager,name='manager_register'),
   path("managerlogin",views.manager_login,name='managerlogin'),
   path("ownerlogin",views.owner_login,name='ownerlogin'),
   path("user_registration",views.register_user,name='user_register')
   
]