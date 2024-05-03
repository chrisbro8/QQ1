# File created by Brownwell
# Edited by Connor (adding routes that I created)

"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from coursework import views
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
    path('admin/', admin.site.urls),
    path('coursework/', include('django.contrib.auth.urls')),
    path('loginpage/', views.loginPage, name="loginpage"),
    path('notify/', views.notify, name="notify"),
    path('profile/', views.profilepage, name="profile"),
    path('settings/', views.settings, name="settings"),
    path('', views.index, name="index"),
    path('loginadmin/', views.loginadmin, name="loginadmin"),
    path('logout/', views.logoutuser, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('register/', views.register, name="register"),
    path('Equipment/', views.equipment, name="Equipment"),
    path('home/', views.home, name="home"),
    path('ViewBookings/', views.ViewBookings, name="ViewBookings"),
    path('nav/', views.navbar, name="navbarPage"),
    path('edituseraccount/', views.EditUserAccount, name="edituseraccount"),
    path('adminviewbookings/', views.AdminViewBookings, name="AdminViewBookings"),
    path('editbookingstatus/<int:booking>/<int:status>/', views.EditBookingStatus),
    path('ad/equipment/register/', views.RegisterEquipment),
    path('ad/equipment/view/', views.ViewEquipment),
    path('ad/equipment/<int:equipmentid>/edit/', views.EditEquipment),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
