from django.urls import path
from .import views

urlpatterns = [

   path("homepage",views.manager_home,name='manager_home')
   
]