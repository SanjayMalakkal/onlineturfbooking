from django.urls import path
from .import views
urlpatterns = [
   path("",views.user_home,name='userhome'),
   path("turfdetails",views.turf_view,name='turfview'),
   path("bookingdetails",views.booking_details,name='details'),
   path("turfbooking",views.turf_booking,name='booking'),
   path("bookinghistory",views.booking_history,name='history')
]