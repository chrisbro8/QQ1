# File created by Brownwell
# Edits made by Connor (adding views created by me)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
''' Home-- Dashboard

'''
def home(request):
    equipments=Equipment.objects.all()
    return render(request, 'coursework/home.html', {'equipments':equipments})
def navbar(request):
    return render(request, 'coursework/navbar.html')
def ViewBookings(request):
    reservations=Reservation.objects.all().order_by('-Booking_madeDate')
    return render(request, 'coursework/ViewBookings.html', {'reservations':reservations})
def EditUserAccount(request):
    user = User.objects.first()
    if request.method == "POST":
        form = EditUserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditUserAccountForm(instance=user)
    return render(request, 'coursework/edituseraccount.html', {'user': user, 'form': form})
def AdminViewBookings(request):
    reservations=Reservation.objects.all().order_by('-Booking_madeDate')
    return render(request, 'coursework/adminviewbookings.html', {'reservations':reservations, 'choices': Reservation.BOOKING_CHOICES})
def EditBookingStatus(request, booking, status):
    reservation = Reservation.objects.get(BookingID=booking)
    reservation.Booking_status = status
    reservation.save()
    return HttpResponse(status=200)
def RegisterEquipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = EquipmentForm()
    return render(request, 'coursework/registerequipment.html', {'form': form, 'title_message': 'Register new equipment'})
def ViewEquipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'coursework/viewequipment.html', {'equipment': equipment, 'locations': Equipment.CHOICES_LOCATION})
def EditEquipment(request, equipmentid):
    equipment = Equipment.objects.get(id=equipmentid)
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'coursework/registerequipment.html', {'form': form, 'title_message': 'Editing "' + equipment.Equipmentname + '"'})
'''def ViewEquipment(request):
    return render(request, 'accounts/ViewEquipment.html')
def EditUserAcc(request):
    return render(request, 'accounts/EditUserAcc.html')
'''