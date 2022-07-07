from django.shortcuts import render
from django.http import HttpResponse

def manager_home(request):
    return render(request,'manager/managerhome.html')

