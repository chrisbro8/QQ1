from django.db import models
from django.apps import apps# imported this to bypass circular dependency
CHOICES_ACCT= (
    (0, 'Current'),
    (1, 'Blocked'),
)



class User(models.Model):
    CHOICES = (
    (0, 'User'),
    (1, 'Not User'),
)
  
    userID = models.CharField(max_length=50, null=True)
    User_firstname = models.CharField(max_length=50, null=True)
    User_lastname = models.CharField(max_length=50, null=True)
    User_Email = models.EmailField(max_length=254, null=True)
    User_password = models.CharField(max_length=50, null=True)
    User_Dateofbirth = models.DateField(auto_now_add=True)
    User_accountstatus = models.IntegerField(null=True,choices=CHOICES_ACCT)
    User_creationDate = models.DateTimeField(auto_now_add=True, null=True)
    User_currentReservation = models.CharField(max_length=50, null=True)
    User_historicalreservation = models.CharField(max_length=50, null=True)
    User_phoneNumber = models.CharField(max_length=13, null=True)
    User_address = models.CharField(max_length=50, null=True)
    UserType = models.IntegerField(null=True, choices=CHOICES)
    def __str__(self):
        return f"{self.User_firstname} {self.User_lastname} {self.UserType}"

class Admin(models.Model):
    adminID = models.CharField(max_length=50, null=True)
    admin_firstname = models.CharField(max_length=50, null=True)
    admin_lastname = models.CharField(max_length=50, null=True)
    admin_username = models.CharField(max_length=50, null=True)
    admin_Email = models.EmailField(max_length=254, null=True)
    admin_password = models.CharField(max_length=50, null=True)
    admin_Dateofbirth = models.DateField(auto_now=True, null=True)
    admin_accountstatus = models.IntegerField(null=True,choices=CHOICES_ACCT)
    admin_creationDate = models.DateTimeField(auto_now_add=True, null=True)
    admin_phoneNumber = models.IntegerField(null=True)
    admin_address = models.CharField(max_length=50, null=True)
    User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Report=models.ForeignKey('Report', null=True, on_delete=models.SET_NULL)
    Reservation = models.ForeignKey('Reservation', null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return f"{self.admin_firstname} {self.admin_lastname}"

class Equipment(models.Model):
    CHOICES_LOCATION = (
        ('Other', 'Other'),
        ('XR Lab', 'XR Lab'),
        ('XR Lab Blue Cabinet', 'XR Lab Blue Cabinet'),
        ('XR Lab Blue Cabinet Large', 'XR Lab Blue Cabinet Large'),
        ('XR medium wooden cabinet', 'XR medium wooden cabinet'),
    )
    CHOICES_USAGE = (
    (0, 'Can be Used and borrowed to home'),
    (1, 'Only used at University'),
    )
    CHOICES_RESTRICT = (
    (0, 'Anyone can use this'),
    (1, 'Can Only be Used by Staff and Admin'),
    )
    CATEGORY= (
    ('PC/Laptop','PC/Laptop'),
    ('VR-Headset','VR Headset'),
    ('Camera/Sensors','Camera/Sensors'),
    ('PC-Peripherals','PC Peripherals'),
    ('Furniture','Furniture'),
    ('Other','Other'),
    ('VR-Controller','VR Controller'),
    ('Phone/Tablets','Phone/Tablets'),
    ('Power/Cable','Power/Cable'),
    ('Non_PortablePC','NonPortablePC'),
    )

    EquipmentID = models.CharField(max_length=50, null=True)
    Equipmentname = models.CharField(max_length=50, null=True)
    Equipment_type = models.CharField(max_length=50, null=True)
    Equipment_category = models.CharField(max_length=50, null=True,choices=CATEGORY)
    Equipment_lastUsed = models.DateTimeField(auto_now_add=True, null=True)
    Equipment_warrantyinfo = models.DateTimeField(auto_now_add=True, null=True)
    Equipment_assignedlocation = models.CharField(max_length=30, null=True, choices=CHOICES_LOCATION)
    Equipment_restrictionStatus = models.IntegerField(null=True, choices=CHOICES_RESTRICT)# 0 No restriction 1  mean
    Equipment_UsageType = models.IntegerField(null=True, choices=CHOICES_USAGE)# 0 meaning can take home 1 meaning it can taken home
    Equipment_images=models.ImageField(null=True,blank=True)

    def __str__(self):
        return f"{self.Equipmentname} {self.Equipment_category}"

class Reservation(models.Model):
    BookingID = models.CharField(max_length=50, null=True)
    Booking_status = models.IntegerField(null=True)
    Booking_alertstatus = models.IntegerField(null=True)
    Booking_madeDate = models.DateTimeField(auto_now_add=True, null=True)
    Booking_startDate = models.DateTimeField(auto_now_add=True, null=True)
    Booking_endDate = models.DateTimeField(auto_now_add=True, null=True)
    User = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    Admin = models.ForeignKey(Admin, null=True, on_delete=models.SET_NULL)
    Equipment = models.ForeignKey(Equipment, null=True,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.BookingID}, User: {self.User.User_firstname} {self.User.User_lastname}"

class Report(models.Model):
    reportKey = models.CharField(max_length=50, null=True)
    lastgeneratedreport = models.DateTimeField(auto_now_add=True, null=True)
    Admin = models.OneToOneField(Admin, null=True, on_delete=models.SET_NULL)
    Reservation = models.ForeignKey(Reservation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "This is a report testing"

class AdminandEquipment(models.Model):
    Admin = models.OneToOneField(Admin, null=True, on_delete=models.SET_NULL)
    Equipment = models.OneToOneField(Equipment, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "This is Admin and Equipment testing"