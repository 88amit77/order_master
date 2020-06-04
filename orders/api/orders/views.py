from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from .models import ManiFest, PODList, NewOrder, Reimburesement, DispatchDetails, FulfilledReturn, RefundImageTable

from .serializers import (
     NewOrderSerializer,
     DispatchDetailsSerializer,
     FulfilledReturnSerializer,
     PODListSerializer,
     ReimburesementSerializer,
     ManiFestSerializer,
     RefundImageTableSerializer,
OrderViewNewOrderSerializer,
updateBinIdSerializer,
updateCancelBinIdSerializer,


                          )
import requests
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

DEFAULT_PAGE = 1
class CustomOrderPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                    'emp_id',
                    'name',
                ],
                'header': {
                    'buymore_order_id':'Buymor Order ID',
                    'dd_id':'DD ID',
                    'product_id':'Product ID',
                    'order_id':'Order ID',
                    'order_item_id' :'Order Item ID',
                    'order_date':'Order Date',
                    'dispatch_by_date' :'Dispatch By Date',
                    'portal_id':'Portal ID',
                    'portal_sku':'Portal SKU',
                    'qty' : 'Quantity',
                    'selling_price' : 'Selling Price',
                    'mrp' :'MRP',
                    'tax_rate' :'Tax Rate',
                    'warehouse_id' : 'Warehouse ID',
                    'region'  : 'Region',
                    'payment_method' : 'Payment Method',
                    'is_canceled':'IS Canceled',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'return_request_date':'Return Request Date',
                    'actual_return_date':'Actual Request Date',
                    'case_id':'Case ID',
                    'status_of_case':'Status Of Case',
                    'reimbursement_amount':'Reimburesement Amount',
                   },
                'sortable': [
                    'buymore_order_id',
                    'dd_id',
                ],

            },
            'results': data
        })

class CustomOrderSearchPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                    'emp_id',
                    'name',
                ],
                'header': {
                    'buymore_order_id':'Buymor Order ID',
                    'dd_id':'DD ID',
                    'product_id':'Product ID',
                    'order_id':'Order ID',
                    'order_item_id' :'Order Item ID',
                    'order_date':'Order Date',
                    'dispatch_by_date' :'Dispatch By Date',
                    'portal_id':'Portal ID',
                    'portal_sku':'Portal SKU',
                    'qty' : 'Quantity',
                    'selling_price' : 'Selling Price',
                    'mrp' :'MRP',
                    'tax_rate' :'Tax Rate',
                    'warehouse_id' : 'Warehouse ID',
                    'region'  : 'Region',
                    'payment_method' : 'Payment Method',
                    'is_canceled':'IS Canceled',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'return_request_date':'Return Request Date',
                    'actual_return_date':'Actual Request Date',
                    'case_id':'Case ID',
                    'status_of_case':'Status Of Case',
                    'reimbursement_amount':'Reimburesement Amount',
                   },
                'sortable': [
                    'buymore_order_id',
                    'dd_id',
                ],
                'searchable': [
                    'buymore_order_id',
                    'dd_id',
                    'product_id',
                    'order_id',
                    'order_item_id',
                    'order_date',
                    'dispatch_by_date',
                    'portal_id',
                    'portal_sku',
                    'qty',
                    'selling_price',
                    'mrp',
                    'tax_rate',
                    'warehouse_id',
                    'region',
                    'payment_method',
                ],

            },
            'results': data
        })


class NewOrderViewSet(viewsets.ModelViewSet):
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer

class DispatchDetailsViewSet(viewsets.ModelViewSet):
    queryset = DispatchDetails.objects.all()
    serializer_class = DispatchDetailsSerializer

class ReimburesementViewSet(viewsets.ModelViewSet):
    queryset = Reimburesement.objects.all()
    serializer_class = ReimburesementSerializer

class FulfilledReturnViewSet(viewsets.ModelViewSet):
    queryset = FulfilledReturn.objects.all()
    serializer_class = FulfilledReturnSerializer


class ManiFestViewSet(viewsets.ModelViewSet):
    queryset = ManiFest.objects.all()
    serializer_class = ManiFestSerializer


class PODListViewSet(viewsets.ModelViewSet):
    queryset = PODList.objects.all()
    serializer_class = PODListSerializer

class RefundImageTableViewSet(viewsets.ModelViewSet):
    queryset = RefundImageTable.objects.all()
    serializer_class = RefundImageTableSerializer

#order view page
class orderviewViewSet(viewsets.ModelViewSet):
    queryset = NewOrder.objects.all()
    serializer_class = OrderViewNewOrderSerializer
    pagination_class = CustomOrderPagination

class ListorderViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = NewOrder.objects.all()
        serializer = OrderViewNewOrderSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomOrderPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = OrderViewNewOrderSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomOrderPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)



class updateBinIdViewSet(viewsets.ModelViewSet):
    queryset = NewOrder.objects.all()
    serializer_class = updateBinIdSerializer
    pagination_class = CustomOrderPagination

class updateCancelBinIdViewSet(viewsets.ModelViewSet):
    queryset = NewOrder.objects.all()
    serializer_class = updateCancelBinIdSerializer
    pagination_class = CustomOrderPagination


class OrderViewSearchAPIView(generics.ListCreateAPIView):
    search_fields = [ 'buymore_order_id', 'dd_id', 'product_id', 'order_id',
    'order_item_id', 'order_date', 'dispatch_by_date', 'portal_id', 'portal_sku',
    'qty', 'selling_price', 'mrp', 'tax_rate', 'warehouse_id', 'region', 'payment_method'
   ]
    ordering_fields = ['buymore_order_id','dd_id']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = NewOrder.objects.all()
    serializer_class = OrderViewNewOrderSerializer
    pagination_class = CustomOrderSearchPagination