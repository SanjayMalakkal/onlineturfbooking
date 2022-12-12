from django.urls import path
from .import views
app_name = 'manager'

urlpatterns = [

   path("",views.manager_home,name='manager_home'),
   path("addturf",views.add_turf,name='addturf'),
   path("viewturf",views.view_turf,name='viewturf'),
   path("viewbooking",views.bookings,name='viewbooking'),
   path("bookinghistory",views.booking_history,name='bookinghistory')
   
]