from django.shortcuts import render
from django.http import HttpResponse
from .models import *
''' Home-- Dashboard

'''
def home(request):
    equipments=Equipment.objects.all()
    return render(request, 'coursework/home.html',{'equipments':equipments})
def navbar(request):
    return render(request, 'coursework/navbar.html')
def ViewBookings(request):
    return render(request, 'coursework/ViewBookings.html')
'''def ViewEquipment(request):
    return render(request, 'accounts/ViewEquipment.html')
def EditUserAcc(request):
    return render(request, 'accounts/EditUserAcc.html')
'''