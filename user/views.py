from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from urllib.request import Request
from django.shortcuts import redirect, render
from .models import *
from login.models import Users
# Create your views here.
def user_home(request):
    user_data = User.objects.get(id = request.session['user_id'])
    
    return render(request,'user/user_home.html',{'user' : user_data})


def turf_view(request):
    return render(request,'user/user_turf_view.html')


def booking_details(request):
    return render(request,'user/booking_details.html')


def turf_booking(request):
    return render(request,'user/book_turf.html')


def booking_history(request):
    return render(request,'user/booking_history.html')


def logout(request):
    del request.session['user_id']
    request.session.flush()
    return redirect('login:home')
