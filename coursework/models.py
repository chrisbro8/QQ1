from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


CHOICES_ACCT = (
    (0, 'Current'),
    (1, 'Blocked'),
)

CHOICES_USER_TYPE = (
    (0, 'User'),
    (1, 'Not User'),
)

CHOICES_BOOKING_STATUS = (
    (0, 'Waiting for approval'),
    (1, 'Approved'),
    (2, 'Denied'),
    (3, 'Waiting to be collected'),
    (4, 'Collected'),
    (5, 'Not returned'),
    (6, 'Returned'),
)

CHOICES_EQUIPMENT_LOCATION = (
    ('Other', 'Other'),
    ('XR Lab', 'XR Lab'),
    ('XR Lab Blue Cabinet', 'XR Lab Blue Cabinet'),
    ('XR Lab Blue Cabinet Large', 'XR Lab Blue Cabinet Large'),
    ('XR medium wooden cabinet', 'XR medium wooden cabinet'),
)

CHOICES_EQUIPMENT_USAGE = (
    (0, 'Can be Used and borrowed to home'),
    (1, 'Only used at University'),
)

CHOICES_EQUIPMENT_RESTRICT = (
    (0, 'Anyone can use this'),
    (1, 'Can Only be Used by Staff and Admin'),
)

CHOICES_EQUIPMENT_CATEGORY = (
    ('PC/Laptop', 'PC/Laptop'),
    ('VR-Headset', 'VR Headset'),
    ('Camera/Sensors', 'Camera/Sensors'),
    ('PC-Peripherals', 'PC Peripherals'),
    ('Furniture', 'Furniture'),
    ('Other', 'Other'),
    ('VR-Controller', 'VR Controller'),
    ('Phone/Tablets', 'Phone/Tablets'),
    ('Power/Cable', 'Power/Cable'),
    ('Non_PortablePC', 'NonPortablePC'),
)

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,default='DEFAULT VALUE')
    userID = models.CharField(max_length=50, blank=True, default='DEFAULT VALUE')
    user_firstname = models.CharField(max_length=50, verbose_name="First Name")
    user_lastname = models.CharField(max_length=50, verbose_name="Last Name")
    user_Email = models.CharField(max_length=254, verbose_name="Email")
    user_password = models.CharField(max_length=50)
    user_Dateofbirth = models.DateField(verbose_name="Date of Birth")
    user_accountstatus = models.IntegerField(choices=CHOICES_ACCT, default=0)
    user_creationDate = models.DateTimeField(default=timezone.now)
    user_currentReservation = models.CharField(max_length=50, blank=True)
    user_historicalreservation = models.CharField(max_length=50, blank=True)
    user_phoneNumber = models.CharField(max_length=13, verbose_name="Phone Number", blank=True)
    user_address = models.CharField(max_length=50, verbose_name="Address", blank=True)
    userType = models.IntegerField(choices=CHOICES_USER_TYPE, default=0)
    profile_pic=models.ImageField(default="person.png",null=True,blank=True)

    def __str__(self):
        return f"{self.user_firstname} {self.user_lastname}"

class Admin(models.Model):
    adminID = models.CharField(max_length=50, default='DEFAULT VALUE')
    admin_firstname = models.CharField(max_length=50)
    admin_lastname = models.CharField(max_length=50)
    admin_username = models.CharField(max_length=50)
    admin_Email = models.CharField(max_length=254)
    admin_password = models.CharField(max_length=50)
    admin_Dateofbirth = models.DateField(default=timezone.now)
    admin_accountstatus = models.IntegerField(choices=CHOICES_ACCT, default=0)
    admin_creationDate = models.DateTimeField(default=timezone.now)
    admin_phoneNumber = models.CharField(max_length=13, blank=True)
    admin_address = models.CharField(max_length=50, blank=True)
    Report = models.ForeignKey('Report', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return f"{self.admin_firstname} {self.admin_lastname}"

class Equipment(models.Model):
    EquipmentID = models.CharField(max_length=50, default='DEFAULT VALUE')
    Equipmentname = models.CharField(max_length=50, verbose_name="Name")
    Equipment_type = models.CharField(max_length=50, verbose_name="Type")
    Equipment_category = models.CharField(max_length=50, choices=CHOICES_EQUIPMENT_CATEGORY, verbose_name="Category")
    Equipment_lastUsed = models.DateTimeField(default=timezone.now)
    Equipment_warrantyinfo = models.DateTimeField(verbose_name="Warranty Info")
    Equipment_assignedlocation = models.CharField(max_length=30, choices=CHOICES_EQUIPMENT_LOCATION, verbose_name="Assigned Location")
    Equipment_restrictionStatus = models.IntegerField(choices=CHOICES_EQUIPMENT_RESTRICT, verbose_name="Restriction")
    Equipment_UsageType = models.IntegerField(choices=CHOICES_EQUIPMENT_USAGE, verbose_name="Take Home?")
    Equipment_images = models.ImageField(upload_to="", verbose_name="Image")
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.Equipmentname} {self.Equipment_category}"

class Reservation(models.Model):
    BookingID = models.CharField(max_length=50, null=True, default='DEFAULT VALUE')
    Booking_status = models.IntegerField(choices=CHOICES_BOOKING_STATUS, null=True)
    Booking_madeDate = models.DateTimeField(default=timezone.now, null=True)
    Booking_startDate = models.DateTimeField(default=timezone.now, null=True)
    Booking_endDate = models.DateTimeField(default=timezone.now, null=True)
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    Admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, default='DEFAULT VALUE')
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.BookingID}, User: {self.Customer.user_firstname} {self.Customer.user_lastname}"

class Report(models.Model):
    reportKey = models.CharField(max_length=50, null=True)
    lastgeneratedreport = models.DateTimeField(default=timezone.now, null=True)
    Admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    Reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "This is a report testing"

class AdminandEquipment(models.Model):
    Admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    Equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "This is Admin and Equipment testing"
