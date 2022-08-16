from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request,'login/log_in.html')


def register_manager(request):
    return render(request,'login/manager_registration.html')


def register_user(request):
    return render(request,'login/user_registration.html')

