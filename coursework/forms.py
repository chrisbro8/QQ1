#File created by Connor (modelforms made: EquipmentForm)

from django.forms import ModelForm
from .models import User, Equipment

class EditUserAccountForm(ModelForm):
    class Meta:
        model = User
        fields = ['User_firstname', 'User_lastname', 'User_Email', 'User_Dateofbirth', 'User_phoneNumber', 'User_address']

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['EquipmentID', 'Equipmentname', 'Equipment_type', 'Equipment_category', 'Equipment_warrantyinfo', 'Equipment_assignedlocation', 'Equipment_restrictionStatus', 'Equipment_UsageType', 'Equipment_images']