import django_filters
from django_filters import DateFilter
from .models import *
from .models import Equipment
##############:since the Image filters dont suppoert image fields it has to be overdien

from django.forms import FileInput
from django.db.models import ImageField


class EquipmentFilter(django_filters.FilterSet):
    Equipment_images = django_filters.CharFilter(widget=FileInput, method='filter_image')
    start_date=DateFilter(field_name="Equipment_lastUsed",lookup_expr='gte')
    end_date=DateFilter(field_name="Equipment_lastUsed",lookup_expr='lte')
    class Meta:
        exclude=['Equipment_images','Equipment_UsageType','Equipment_warrantyinfo','Equipment_restrictionStatus','Equipment_assignedlocation']
        model = Equipment
        fields = '__all__'

    def filter_image(self, queryset, name, value):
        # Implement your filter logic here
        # For example, filtering by Equipment images filename
        return queryset.filter(**{f'{name}__icontains': value})
