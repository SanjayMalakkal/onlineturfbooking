from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from login.models import Users
from login.models import Turfmanager
from .models import *

def owner_home(request):
    return render(request,'owner/owner_home.html')


def manager_details(request):
    return render(request,'owner/manager_details.html')


def manager_approval(request):
    return render(request,'owner/manager_approval.html')

def user_details(request):
    return render(request,'owner/user_details.html')

def logout(request):
    # del request.session['user_id']
    # request.session.flush()
    return redirect('login:ownerlogin')

def load_manager(request):
    managers = Turfmanager.objects.filter(manager_status='pending')
    data = [{'id': manager.id, 'name': manager.manager_name, 'email': manager.manager_email,
             'address': manager.manager_address, 'phone': manager.manager_phone,'image': manager.manager_image.url} for manager in managers]
             
    print(data)
    return JsonResponse({'data': data})

def delete_manager(request):
    id = request.POST['id']
    manager = Turfmanager.objects.get(id=id)
    manager.delete()
    return JsonResponse({'status': 'manager deleted'})

def manager_approvals(request):
    id = request.POST['id']
    manager = Turfmanager.objects.get(id=id)
    manager.manager_status='approved'
    manager.save()
    send_mail(
    'Approved',
    'Hi we are pleased to inform you that user request has been approved.',
    'sanjayproject222@gmail.com',
    [manager.manager_email],
    fail_silently=False,
)
    return JsonResponse({'status': 'manager approved'})


def user_available(request):
    users = Users.objects.all()
    data = [{'id': user.id, 'name': user.user_name, 'email': user.user_email,
              'phone': user.user_phone} for user in users]
             
    print(data)
    return JsonResponse({'data': data})

def approved_manager(request):
    managers = Turfmanager.objects.filter(manager_status='approved')
    data = [{'id': manager.id, 'name': manager.manager_name, 'email': manager.manager_email,
             'address': manager.manager_address, 'phone': manager.manager_phone, 'image': manager.manager_image.url} for manager in managers]
             
    print(data)
    return JsonResponse({'data': data})

