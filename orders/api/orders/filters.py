from django_filters import rest_framework as filters

from .models import NewOrder


class OrderDateFilter(filters.FilterSet):
    order_date = filters.DateFromToRangeFilter()

    class Meta:
        model = NewOrder
        fields = ['order_date']

class DispatchByDateFilter(filters.FilterSet):
    dispatch_by_date = filters.DateFromToRangeFilter()

    class Meta:
        model = NewOrder
        fields = ['dispatch_by_date']