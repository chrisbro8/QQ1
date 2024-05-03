# File created by Brownwell
# Edits made by Connor (adding views created by me)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import CreateUserForm,CustomerForm
from django.contrib import messages
from .filters import *
from .decorators import unauthenticated_user,allowed_users


#from .filters import OrderFilter
@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['Staff','user'])
def home(request):
    equipments=Equipment.objects.all()
    return render(request, 'home.html', {'equipments':equipments})


def loginPage(request):
   
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
    context={}
    return render(request, 'login.html',context)

def loginadmin(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
    
        if user is not None:
            login(request,user)

            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')

    context={}
    return render(request, 'loginadmin.html',context)




def index(request):
    return render(request,'index.html')












@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('loginpage')



def register(request):
    
    form=CreateUserForm(request.POST)

    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='user')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
            )
            
            messages.success(request,'Account was created for'+username)
            return redirect('loginpage')
    context={'form':form}
    return render(request, 'UserRegister.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff','user'])
def equipment(request):
    filtered_equipment=Equipment.objects.all()
    myFilter=EquipmentFilter(request.GET,queryset=filtered_equipment)
    filtered_equipment=myFilter.qs
    context={'filtered_equipment':filtered_equipment,'myFilter':myFilter}
    return render(request, 'equipment.html',context)


@unauthenticated_user
def navbar(request):
    return render(request, 'navbar.html')

@unauthenticated_user
@allowed_users(allowed_roles=['Staff','user'])
def ViewBookings(request):
    reservations=Reservation.objects.all().order_by('-Booking_madeDate')
    return render(request, 'ViewBookings.html', {'reservations':reservations})

@unauthenticated_user
@allowed_users(allowed_roles=['Staff','user'])
def EditUserAccount(request):
    user = User.objects.first()
    if request.method == "POST":
        form = EditUserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditUserAccountForm(instance=user)
    return render(request, 'edituseraccount.html', {'user': user, 'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def AdminViewBookings(request):
    reservations=Reservation.objects.all().order_by('-Booking_madeDate')
    return render(request, 'adminviewbookings.html', {'reservations':reservations, 'choices': Reservation.BOOKING_CHOICES})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff','user'])
def EditBookingStatus(request, booking, status):
    reservation = Reservation.objects.get(BookingID=booking)
    reservation.Booking_status = status
    reservation.save()
    return HttpResponse(status=200)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff','user'])
def cart(request):
    return render(request,'cart.html')

@login_required(login_url='login')
def profilepage(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Staff','user'])
def notify(request):
    return render(request,'notify.html')




@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def RegisterEquipment(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = EquipmentForm()
    return render(request, 'registerequipment.html', {'form': form, 'title_message': 'Register new equipment'})

@unauthenticated_user
@allowed_users(allowed_roles=['Staff','user'])
def ViewEquipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'viewequipment.html', {'equipment': equipment, 'locations': Equipment.CHOICES_LOCATION})

@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def EditEquipment(request, equipmentid):
    equipment = Equipment.objects.get(id=equipmentid)
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'registerequipment.html', {'form': form, 'title_message': 'Editing "' + equipment.Equipmentname + '"'})

def settings(request):
	return render(request, 'settings.html')







'''def ViewEquipment(request):
    return render(request, 'accounts/ViewEquipment.html')
def EditUserAcc(request):
    return render(request, 'accounts/EditUserAcc.html')
'''