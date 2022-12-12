from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .models import *

def home(request):
    return render(request,'login/common_home.html')


def login(request):
    msg=''
    if request.method == 'POST':
        u_name = request.POST['email']
        u_pass = request.POST['password']
        data_exits=User.objects.filter(user_email=u_name,user_password=u_pass).exists()
        if data_exits:
            user_data=Users.objects.get(user_email=u_name,user_password=u_pass)
            request.session['user_id']=user_data.id
            request.session['user_name']=user_data.user_name
            msg='logged in successfully'
            return render(request,'login/common_home.html',{'message':msg})
        else:
            msg='incorrect username or password'

    return render(request,'login/log_in.html',{'message':msg})


def manager_login(request):
    msg=''
    if request.method == 'POST':
        m_name = request.POST['username']
        m_pass = request.POST['password']
        manager_exists=Turfmanager.objects.filter(manager_email=m_name,manager_password=m_pass).exists()
        if manager_exists:
            manager_data=Turfmanager.objects.get(manager_email=m_name,manager_password=m_pass)
            if manager_data.manager_status== 'approved':
                request.session['manager_id']=manager_data.id
                return redirect('manager:manager_home')
            else:
                msg = 'Not approved by admin'
            
        else:
            msg='incorrect username or password'

    return render(request,'login/manager_login.html',{'message':msg})


def register_manager(request):

    msg=''
    if request.method == 'POST':
        m_name = request.POST['name']
        m_eml = request.POST['email']
        m_phone = request.POST['number']
        m_passw = request.POST['password']
        m_address = request.POST['address']
        m_file = request.FILES['picture']
        
       
        manager_exists=Turfmanager.objects.filter(manager_email=m_eml).exists()
        if not manager_exists:

             obj = Turfmanager(manager_name=m_name,manager_email=m_eml,manager_password=m_passw,manager_phone=m_phone,manager_address=m_address,manager_image=m_file)
             obj.save()
             msg='Registration successfull'

        
        else:
            msg='email already exist'

    return render(request,'login/manager_registration.html',{'message':msg})


def register_user(request):

    msg=''
    if request.method == 'POST':
        u_name = request.POST['name']
        u_eml = request.POST['email']
        U_passw = request.POST['password']
        u_phone = request.POST['telephone']
       
        user_exists=Users.objects.filter(user_email=u_eml).exists()
        if not user_exists:

             obj = Users(user_name=u_name,user_email=u_eml,user_password=U_passw,user_phone=u_phone)
             obj.save()
             msg='Registration successfull'

        
        else:
            msg='email already exist'

    return render(request,'login/user_registration.html',{'message':msg})


def owner_login(request):
    msg=''
    if request.method == 'POST':
        a_name = request.POST['username']
        a_pass = request.POST['password']
        data_exits=Admin.objects.filter(admin_id=a_name,admin_password=a_pass).exists()
        if data_exits:
            admin_data=Admin.objects.get(admin_id=a_name,admin_password=a_pass)
            request.session['admin_id']=admin_data.id
            return redirect('owner:owner_home')
        else:
            msg='incorrect username or password'
    return render(request,'login/owner_login.html',{'message':msg})





