#File created by Brownwell
from django.forms import ModelForm
from .models import Equipment,User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import *
from django import forms

# class EditUserAccountForm(ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['user_address', 'user_firstname', 'user_Email', 'user_phonenumber', 'user_lastname', 'user_Dateofbirth']


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['EquipmentID', 'Equipmentname', 'Equipment_type', 'Equipment_category', 'Equipment_warrantyinfo', 'Equipment_assignedlocation', 'Equipment_restrictionStatus', 'Equipment_UsageType', 'Equipment_images']
        
# class OrderForm(ModelForm):
#     class meta:
#         model=Order
#         fields='_all_'
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username','email','password1','password2']
        

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user','user_accountstatus','userType','userID','user_creationDate']
