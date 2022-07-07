from django.shortcuts import render
from django.http import HttpResponse

def managerhome(request):
    return render(request,'manager/managerhome.html')
