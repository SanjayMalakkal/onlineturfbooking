from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,'login/login_in.html')


def manager_register(request):
    return render(request,'login/registration_manager.html')


def user_register(request):
    return render(request,'login/registration_user.html')
