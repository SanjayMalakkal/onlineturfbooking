from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def userhome(request):
    return render(request,'user/user_home.html')
