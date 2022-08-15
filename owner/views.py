from django.shortcuts import render
from django.http import HttpResponse

def owner_home(request):
    return render(request,'owner/owner_home.html')


def manager_details(request):
    return render(request,'owner/manager_details.html')


def manager_approval(request):
    return render(request,'owner/manager_approval.html')

def user_details(request):
    return render(request,'owner/user_details.html')

