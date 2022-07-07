from django.urls import path
from .import views
urlpatterns = [
   path("homepage",views.userhome,name='userhome')
]