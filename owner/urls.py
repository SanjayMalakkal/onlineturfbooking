from django.urls import path
from .import views
urlpatterns = [
   path("homepage",views.owner_home,name='ownerhome'),
   path("managerdetails",views.manager_details,name='details'),
   path("managerapproval",views.manager_approval,name='approvals')
]