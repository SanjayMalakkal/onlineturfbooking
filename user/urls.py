from django.urls import path
from .import views
urlpatterns = [
   path("homepage",views.user_home,name='userhome')
]