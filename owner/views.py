from django.shortcuts import render
from django.http import HttpResponse

def ownerhome(request):
    return render(request,'owner/ownerhome.html')


