from django.urls import path
from .import views
urlpatterns = [
   path("homepage",views.owner_home,name='ownerhome')
]