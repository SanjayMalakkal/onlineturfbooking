from django.shortcuts import render
from django.http import HttpResponse

def owner_home(request):
    return render(request,'owner/owner_home.html')


