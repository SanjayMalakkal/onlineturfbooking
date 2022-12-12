from django.shortcuts import render
from django.http import HttpResponse

def manager_home(request):
    return render(request,'manager/manager_home.html')


def add_turf(request):
    return render(request,'manager/add_turf.html')


def view_turf(request):
    return render(request,'manager/view_turf.html')


def bookings(request):
    return render(request,'manager/manager_booking_details.html')



def booking_history(request):
    return render(request,'manager/booking_history.html')
