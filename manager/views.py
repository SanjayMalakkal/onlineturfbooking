from django.shortcuts import render
from django.http import HttpResponse

def manager_home(request):
    return render(request,'manager/manager_home.html')


def add_turf(request):
    return render(request,'manager/add_turf.html')


def turf_updations(request):
    return render(request,'manager/updations.html')
