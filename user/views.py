from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def user_home(request):
    return render(request,'user/user_home.html')


def turf_view(request):
    return render(request,'user/user_turf_view.html')


def booking_details(request):
    return render(request,'user/booking_details.html')


def turf_booking(request):
    return render(request,'user/book_turf.html')


def booking_history(request):
    return render(request,'user/booking_history.html')
