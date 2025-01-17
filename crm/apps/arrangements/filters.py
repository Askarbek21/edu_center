from django_filters import rest_framework as filters

from .models import Group

class GroupFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    status = filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model = Group
        fields = ['name', 'status']