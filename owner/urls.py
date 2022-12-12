from django.urls import path
from .import views
app_name = 'owner'

urlpatterns = [
   path("owner_home",views.owner_home,name='owner_home'),
   path("managerdetails",views.manager_details,name='details'),
   path("managerapproval",views.manager_approval,name='approvals'),
   path("userdetails",views.user_details,name='userdetails'),
   # path("users",views.user_available,name='users'),
   path("deletemanager",views.delete_manager,name='deletemanager'),
   path("managerapprovals",views.manager_approvals,name='managerapprovals'),
   path("log_out",views.logout,name='log_out'),
   path("loadmanager",views.load_manager,name='loadmanager'),
   path("availableuser",views.user_available,name='availableuser'),
   path("approvedmanager",views.approved_manager,name='approvedmanager'),

]