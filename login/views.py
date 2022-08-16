from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def login(request):
    return render(request,'login/login_in.html')


def user_registration(request):
    return render(request,'login/registration_user.html')


def manager_registration(request):
    return render(request,'login/registration_manager.html')
