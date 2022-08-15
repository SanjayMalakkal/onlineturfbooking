from django.urls import path
from .import views

urlpatterns = [

   path("",views.manager_home,name='manager_home'),
   path("addturf",views.add_turf,name='addturf'),
   path("updations",views.turf_updations,name='update')
   
]