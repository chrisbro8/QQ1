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
        form = RegisterEquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['Equipment_images'] = form.cleaned_data['Equipment_images'].split()
            form.save()
            return redirect('/')
        print(form.errors)
    form = RegisterEquipmentForm()
    return render(request, 'coursework/registerequipment.html', {'form': form})
'''def ViewEquipment(request):
    return render(request, 'accounts/ViewEquipment.html')
def EditUserAcc(request):
    return render(request, 'accounts/EditUserAcc.html')
'''