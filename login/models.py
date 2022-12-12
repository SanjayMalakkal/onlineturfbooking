from django.db import models
from distutils.command.upload import upload
from email.policy import default
from unittest.util import _MAX_LENGTH

class Admin(models.Model):
    admin_id = models.IntegerField()
    admin_password = models.CharField(max_length=20)


class User(models.Model):
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)
    user_phone = models.BigIntegerField()
    
class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)
    user_phone = models.BigIntegerField()

class Managers(models.Model):
    manager_name = models.CharField(max_length=50)
    manager_address = models.CharField(max_length=100)
    manager_email = models.CharField(max_length=50)
    manager_password = models.CharField(max_length=20)
    manager_image = models.ImageField(upload_to='manager/')
    manager_phone = models.BigIntegerField()
    manager_status = models.CharField(max_length=40,default='pending')

class Turfmanager(models.Model):
    manager_name = models.CharField(max_length=50)
    manager_address = models.CharField(max_length=100)
    manager_email = models.CharField(max_length=50)
    manager_password = models.CharField(max_length=20)
    manager_image = models.ImageField(upload_to='manager/')
    manager_phone = models.BigIntegerField()
    manager_status = models.CharField(max_length=40,default='pending')
