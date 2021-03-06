from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
import dropbox

access_token = 'd7ElXR2Sr-AAAAAAAAAAC2HC0qc45ss1TYhRYB4Jy6__NJU1jjGiffP7LlP_2rrf'
dbx = dropbox.Dropbox(access_token)

from .models import (ManiFest, PODList, NewOrder, Reimburesement, DispatchDetails, FulfilledReturn, RefundImageTable,
    Reimbursement, TestingStatus,TestingNames,ExternalApiList,ExternalApiLog,CalculationApiList,CalculationApiLog)

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
     ReturnManagementPODListSerializer,
     CreateCaseStatusSerializer,
     CaseStatusListSerializer,
     CreateManiFestSerializer,
     ManifestListSerializer,
     NewOrderCaseStatusSearchSerializer,
     DispathSerializer,
     OrderReturnSerializer,
     OrderReturnProcessSerializers,
     TestingNamesSerializer,
     TestingStatusSerializer,
     ListTestingNames1Serializer,
     TestUpdateSerializer,
     ListEXTAPISerializer,
     ListCALAPISerializer,
     ExternalApiListSerializer,
     ExternalApiLogSerializer,
     CalculationApiListSerializer,
     CalculationApiLogSerializer,
     UpdateExternalApiListSerializer,
     UpdateCalculationApiListSerializer,
     SerachReturnProcessingSerializer,
     MasterSearchTestingSerializer,
DynamicFieldsNewOrdersModelSerializer,
DynamicFieldsReturnsModelSerializer,
 )
import requests
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
import dropbox


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
                    # 'buymore_order_id':'Buymore Order ID',
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
                    'status': "Order Status",
                    'is_canceled':'IS Canceled',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'return_request_date':'Return Request Date',
                    'actual_return_date':'Actual Request Date',
                    'case_id':'Case ID',
                    'status_of_case':'Status Of Case',
                    'reimbursement_amount': 'Reimburesement Amount',
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
                    # 'buymore_order_id':'Buymore Order ID',
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
                    'status': "Order Status",
                    'is_canceled':'IS Canceled',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'return_request_date':'Return Request Date',
                    'actual_return_date':'Actual Request Date',
                    'case_id':'Case ID',
                    'status_of_case':'Status Of Case',
                    'reimbursement_amount':'Reimburesement Amount',
                   },
                'sortable': [
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
                'searchable': [
                    # 'buymore_order_id',
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

class CustomRMPODListPagination(PageNumberPagination):
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
                    'pod_id',
                    'pod_number',
                    'courier_partner_name',
                ],
                'header': {
                    'pod_id':'POD ID',
                    'pod_number':'POD Number',
                    'courier_partner_name':'Courier Partner Name',
                    'pod_image_list':'POD Image List',
                    'total_quantity_received' :'Total Quantity Received',
                    'processed_quantity':'Processed Quantity',
                    'warehouse_id' :'Warehouse ID',
                    'courier_received_date': 'Courier Received Date',
                    'created_by': 'Created By',
                    'status': 'Status',
                    'updated_at': 'Updated At',
                    'remaining_quantity':'Remaining Quantity',
                    'warehouse_name':'Warehouse Name',
                    'recieved_by':'Recieved By',


                   },
                'sortable': [
                    'pod_id',
                    'pod_number',
                ],
                'searchable': [
                     'pod_id',
                     'pod_number',
                     'courier_partner_name',
                     'pod_image_list',
                     'total_quantity_received',
                     'processed_quantity',
                     'warehouse_id',
                     'courier_received_date',
                     'created_by',
                     'status',
                     'updated_at',
                ],

            },
            'results': data
        })

class CustomRMPODListWHPagination(PageNumberPagination):
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
                    'pod_id',
                    'pod_number',
                    'courier_partner_name',
                ],
                'header': {
                    'pod_id':'POD ID',
                    'pod_number':'POD Number',
                    'courier_partner_name':'Courier Partner Name',
                    'pod_image_list':'POD Image List',
                    'total_quantity_received' :'Total Quantity Received',
                    'processed_quantity':'Processed Quantity',
                    'warehouse_id' :'Warehouse ID',
                    'courier_received_date': 'Courier Received Date',
                    'created_by': 'Created By',
                    'status': 'Status',
                    'updated_at': 'Updated At',
                    'remaining_quantity':'Remaining Quantity',
                    'warehouse_name':'Warehouse Name',
                    'recieved_by':'Recieved By',


                   },
                'sortable': [
                    'pod_id',
                    'pod_number',
                ],
                'searchable': [

                     'warehouse_id',

                ],

            },
            'results': data
        })

class CustomCaseStatusPagination(PageNumberPagination):
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
                    'case_id',

                ],
                'header': {
                    # 'rr_id' : 'RR ID',
                    # 'dd_id' : 'DD ID',
                    'case_id' : 'Case ID',
                    'status_of_case':'Status Of Case',
                    # 'case_content' :'Case Content',
                    # 'case_reply':'Case Reply',
                    'reimbursement_amount' :'Reimbursement Amount',
                    'quantity':'Quantity',

                   },
                'sortable': [
                    'case_id',
                ],
                'searchable': [
                    'case_id',
                    'status_of_case',
                    'reimbursement_amount',
                ],

            },
            'results': data
        })

class CustomManiFestPagination(PageNumberPagination):
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
                    'mf_id',

                ],
                'header': {
                    'mf_id':'Manifest Id',
                    'courier_partner':'Courier',
                    'created_date':'Date',
                    'quantity':'Quantity',

                   },
                'sortable': [
                    'mf_id',
                ],
                'searchable': [
                     'mf_id',
                    'courier_partner',
                    'created_date',
                    'created_date',
                    'quantity',
                ],

            },
            'results': data
        })

class CustomOrderReturnPagination(PageNumberPagination):
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
                # 'sticky_headers': [
                #     'emp_id',
                #     'name',
                # ],
                'header': {
                    'order_id':'Order ID',
                    'order_item_id' :'Order Item ID',
                    'order_date':'Order Date',
                    'dispatch_by_date' :'Dispatch By Date',

                    'warehouse_id': 'Warehouse ID',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'courier_partner': 'Courier Partner Name',
                    'return_request_date': 'Return Request Date',
                    'actual_return_date': 'Actual Return Date',
                    'return_reason': 'Return Reason',
                    'sub_reason': 'Sub Reason',
                    'awb': 'AWB',
                    'pod_id': 'POD ID',
                    'return_type': 'Return Type',
                    'product_condition': 'Product Condition',
                    'package_condition':'Package Condition',
                    'image_correctness':'Image Correctness',
                    'size_correctness': 'Size Correctness',
                    'alternate_product_id':'Alternate Product_id',
                    'image_list': 'Image List',

                   },
                # 'sortable': [
                #
                #     'dd_id',
                # ],
                'searchable': [
                                'order_id',
                                'order_item_id',
                                'order_date',
                                'dispatch_by_date',
                                'portal_sku',
                                'warehouse_id',
                                'cancel_inward_bin',
                                 'courier_partner',
                                'return_request_date',
                                'actual_return_date',
                                'return_reason',
                                'sub_reason',
                                'awb',
                                # 'pod_id',
                                'return_type',
                                'product_condition',
                                'package_condition',
                                'image_correctness',
                                'image_list',
                                'alternate_product_id',
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


#for cross check FR id is present or not
class SearchFulfilledReturnViewSet(viewsets.ModelViewSet):
    search_fields = ['=fr_id', ]
    filter_backends = (filters.SearchFilter,)
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
    search_fields = [ 'dd_id', 'product_id', 'order_id',
    'order_item_id', 'order_date', 'dispatch_by_date', 'portal_id', 'portal_sku',
    'qty', 'selling_price', 'mrp', 'tax_rate', 'warehouse_id', 'region', 'payment_method'
   ]
    ordering_fields = ['dd_id', 'product_id', 'order_id',
    'order_item_id', 'order_date', 'dispatch_by_date', 'portal_id', 'portal_sku',
    'qty', 'selling_price', 'mrp', 'tax_rate', 'warehouse_id', 'region', 'payment_method']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = NewOrder.objects.all()
    serializer_class = OrderViewNewOrderSerializer
    pagination_class = CustomOrderSearchPagination


#ReturnManagement POD list page
class CreateRMPODlistViewSet(viewsets.ModelViewSet):
    queryset = PODList.objects.all()
    serializer_class = ReturnManagementPODListSerializer


class ListRMPODlistViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = PODList.objects.all()
        serializer = PODListSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomRMPODListPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PODListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomRMPODListPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class SearchListRMPODlistViewSet(generics.ListCreateAPIView):
    search_fields = [ 'pod_id',
                     'pod_number',
                     'courier_partner_name',
                     'pod_image_list',
                     'total_quantity_received',
                     'processed_quantity',
                     'warehouse_id',
                     'courier_received_date',
                     'created_by',
                     'status',
                     'updated_at',
   ]
    ordering_fields = ['pod_id','pod_number']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = PODList.objects.all()
    serializer_class = PODListSerializer
    pagination_class = CustomRMPODListPagination


class SearchListRMPODlistWarehouseViewSet(generics.ListCreateAPIView):
    search_fields = ['warehouse_id', ]
    ordering_fields = ['pod_id', 'pod_number']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter )
    queryset = PODList.objects.all()
    serializer_class = PODListSerializer
    pagination_class = CustomRMPODListWHPagination


#order case status
class NewOrderCaseStatusSearchViewSet(generics.ListCreateAPIView):
    search_fields = [
                    '=order_id', '=order_item_id','=product_id',
                     ]
    filter_backends = (filters.SearchFilter,)
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderCaseStatusSearchSerializer

class CreateordercasestatusViewSet(viewsets.ModelViewSet):
    queryset = Reimbursement.objects.all()
    serializer_class = CreateCaseStatusSerializer

class ListordercasestatusViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = Reimbursement.objects.all()
        serializer = CaseStatusListSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomCaseStatusPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CaseStatusListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomCaseStatusPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class SearchListordercasestatusViewSet(generics.ListCreateAPIView):
    search_fields = [
                    'case_id',
                    'status_of_case',
                    'reimbursement_amount',
                     ]
    ordering_fields = ['case_id',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Reimbursement.objects.all()
    serializer_class = CreateCaseStatusSerializer
    pagination_class = CustomCaseStatusPagination


#manifest
class NewOrderManifestSearchViewSet(generics.ListCreateAPIView):
    search_fields = ['=awb']
    filter_backends = (filters.SearchFilter,)
    queryset = DispatchDetails.objects.all()
    serializer_class = DispathSerializer

class CreateManiFestViewSet(viewsets.ModelViewSet):
    queryset = ManiFest.objects.all()
    serializer_class = CreateManiFestSerializer

class ListManiFestViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = ManiFest.objects.all()
        serializer = ManifestListSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomManiFestPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ManifestListSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomManiFestPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)


class SearchListManiFestViewSet(generics.ListCreateAPIView):
    search_fields = [
                    'mf_id',
                    'courier_partner',
                    'created_date',

                     ]
    ordering_fields = ['mf_id',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = ManiFest.objects.all()
    serializer_class = ManifestListSerializer
    pagination_class = CustomManiFestPagination

#customise search and date filter api for new order
class SearchOrderIDViewSet(generics.ListCreateAPIView):
    search_fields = ['=order_id']
    filter_backends = (filters.SearchFilter, )
    queryset = NewOrder.objects.all()
    serializer_class = NewOrderSerializer

from rest_framework.viewsets import ViewSet
from .filters import OrderDateFilter, DispatchByDateFilter


class OrderDateFilterViewSet(ViewSet):
    """
    how use query parameter
    http://127.0.0.1:8000/neworder2/dispatch_by_date_filter/?dispatch_by_date_after=2001-02-01&dispatch_by_date_before=2020-02-02
    """
    def list(self, request):
        queryset = NewOrder.objects.all()
        queryset = OrderDateFilter(data=request.GET, queryset=queryset, request=request).qs
        serializer = NewOrderSerializer(queryset, many=True)
        return Response(serializer.data)

class DispatchByDateFilterViewSet(ViewSet):
    def list(self, request):
        queryset = NewOrder.objects.all()
        queryset = DispatchByDateFilter(data=request.GET, queryset=queryset, request=request).qs
        serializer = NewOrderSerializer(queryset, many=True)
        return Response(serializer.data)

#order return page

#to search order_id is present or not including FR_id
class SerachReturnProcessingViewSet(viewsets.ModelViewSet):
    search_fields = [
        '=order_id',
       ]
    filter_backends = (filters.SearchFilter, )
    queryset = NewOrder.objects.all()
    serializer_class = SerachReturnProcessingSerializer

class ListOrderReturnViewSet(viewsets.ViewSet):
    def create(self, request):
        queryset = NewOrder.objects.all()
        serializer = OrderReturnSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomOrderReturnPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = OrderReturnSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomOrderReturnPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class updateIdViewSet(viewsets.ModelViewSet):
    search_fields = [
        'order_id',
        'order_item_id',
        'order_date',
        'dispatch_by_date',
        'warehouse_id',
        'dd_dispatchdetailss__cancel_inward_bin',
        'dd_dispatchdetailss__courier_partner',
        'dd_fullfilledreturn__return_request_date',
        'dd_fullfilledreturn__actual_return_date',
        'dd_fullfilledreturn__return_reason',
        'dd_fullfilledreturn__sub_reason',
        'dd_fullfilledreturn__awb',
        # 'dd_fullfilledreturn__pod_id',
        'dd_fullfilledreturn__return_type',
        'dd_refundimagetable__product_condition',
        'dd_refundimagetable__package_condition',
        'dd_refundimagetable__image_correctness',
        'dd_refundimagetable__size_correctness',
        'dd_refundimagetable__alternate_product_id',
         'dd_refundimagetable__image_list',
    ]
    ordering_fields = ['order_id']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = NewOrder.objects.all()
    serializer_class = OrderReturnSerializer
    pagination_class = CustomOrderReturnPagination


#order return process page
class OrderReturnProcessViewSet(viewsets.ModelViewSet):
    queryset = RefundImageTable.objects.all()
    serializer_class = OrderReturnProcessSerializers


#Testin name and status
class CustomTestingPagination(PageNumberPagination):
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
                               'tn_id',
                               'name',
                                         ],
                'header': {
                              'tn_id': 'ID',
                              "tn_name": 'Name',
                              "average_time": 'Average Time',
                              # "tn_cron_code": 'Cron Code',
                              # "tn_type": 'Type',
                              "ts_starttime": 'Start Time',
                              # "ts_startfile": 'Start File',
                              "ts_stoptime": 'Stop Time',
                              # "ts_stopfilelog": 'Stop File',
                              "ts_status": 'Status',



                           },
                'searchable': [
                    'tn_name',
                    # 'average_time',
                    # 'ts_starttime',
                    # 'ts_stoptime',
                    # 'ts_status',
                    'tn_type',
                ],
                'sortable': [
                              'tn_id','tn_name','ts_starttime','ts_stoptime',
                           ],


            },
            'results': data
        })
class TestingNamesViewSet(viewsets.ModelViewSet):

    queryset = TestingNames.objects.all()
    serializer_class = TestingNamesSerializer



class TestingStatusViewSet(viewsets.ModelViewSet):

    queryset = TestingStatus.objects.all()
    serializer_class = TestingStatusSerializer



class ListAssignRulesViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = TestingNames.objects.all()
        serializer = ListTestingNames1Serializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomTestingPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListTestingNames1Serializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomTestingPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchTestViewSet(viewsets.ModelViewSet):
    search_fields = [
        '=tn_type',
        # 'tn_name',
        # 'average_time',
        # 'testing_statuss__ts_starttime',
        # 'testing_statuss__ts_stoptime',
        # 'testing_statuss__ts_status',

    ]
    ordering_fields = ['tn_name','tn_id','testing_statuss__ts_starttime','testing_statuss__ts_stoptime']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = TestingNames.objects.all()
    serializer_class = ListTestingNames1Serializer
    pagination_class = CustomTestingPagination


#for master search for testing page
class EmployeeWiseAttendanceLogViewSet(viewsets.ModelViewSet):
    search_fields = ['=tn_type','tn_name']
    ordering_fields = ['tn_id','tn_name','testing_statuss__ts_starttime','testing_statuss__ts_stoptime','testing_statuss__ts_status']
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = TestingNames.objects.all().order_by('-testing_statuss__ts_starttime')
    serializer_class = MasterSearchTestingSerializer
    pagination_class = CustomTestingPagination




from django_filters.rest_framework import DjangoFilterBackend

class SearchTestViewSet22(generics.ListAPIView):
    queryset = TestingNames.objects.all()
    serializer_class = ListTestingNames1Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tn_type', 'tn_name']
    pagination_class = CustomTestingPagination

class UpdateTestViewSet(viewsets.ModelViewSet):

    queryset = TestingNames.objects.all()
    serializer_class = TestUpdateSerializer
    pagination_class = CustomTestingPagination

#API LOgs page
class CustomEXTAPIPagination(PageNumberPagination):
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
                    'eal_portal_id',
                    'eal_name',

                ],
                'header': {
                    'eal_portal_id' : 'Portal Name',
                    'eal_name' : 'API Name',
                    'eal_account_id' : 'Account',
                    'eal_average_time': 'Average Time',
                    'eal_start_time' : 'Start Time',
                    'eal_end_time':'End Time',
                    'eal_user_id' :'User ID',


                   },
                'sortable': [
                    'eal_name',
                ],
                'searchable': [
                    'eal_portal_id',
                    'eal_name',
                    'eal_account_id',
                    'eal_average_time',
                    'eal_start_time',
                    'eal_end_time',
                    'eal_user_id',
                ],

            },
            'results': data
        })

class CustomCALAPIPagination(PageNumberPagination):
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
                    'cal_name',

                ],
                'header': {
                    'cal_name': 'Calculation Name',
                    'cal_average_time': 'Average Time',
                    'cal_start_time': 'Start Time',
                    'cal_end_time': 'End Time',
                    'cal_user_id': 'User ID',
                    },
                'sortable': [
                    'cal_name',
                ],
                'searchable': [
                    'cal_name',
                    'cal_average_time',
                    'cal_start_time',
                    'cal_end_time',
                    'cal_user_id',
                ],

            },
            'results': data
        })


## amit_view for four extaa added tables
class ExternalApiListViewSet(viewsets.ModelViewSet):
	queryset = ExternalApiList.objects.all()
	serializer_class = ExternalApiListSerializer


class ExternalApiLogViewSet(viewsets.ModelViewSet):
	queryset = ExternalApiLog.objects.all()
	serializer_class = ExternalApiLogSerializer

class CalculationApiListViewSet(viewsets.ModelViewSet):
	queryset = CalculationApiList.objects.all()
	serializer_class = CalculationApiListSerializer

class CalculationApiLogViewSet(viewsets.ModelViewSet):
	queryset = CalculationApiLog.objects.all()
	serializer_class = CalculationApiLogSerializer


class ListEXTAPIViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = ExternalApiList.objects.all()
        serializer = ListEXTAPISerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomEXTAPIPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListEXTAPISerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomEXTAPIPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchEXTAPIViewSet(viewsets.ModelViewSet):
    search_fields = [

        'eal_portal_id',
        'eal_name',
        'eal_account_id',
        'eal_average_time',
        'ext_log__eal_start_time',
        'ext_log__eal_end_time',
        'ext_log__eal_user_id',

    ]
    ordering_fields = ['eal_name',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = ExternalApiList.objects.all()
    serializer_class = ListEXTAPISerializer
    pagination_class = CustomEXTAPIPagination
class ListCALAPIViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = CalculationApiList.objects.all()
        serializer = ListCALAPISerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomCALAPIPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListCALAPISerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomCALAPIPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchCalAPIViewSet(viewsets.ModelViewSet):
    search_fields = [

                    'cal_name',
                    'cal_average_time',
                    'cal_logs__cal_start_time',
                    'cal_logs__cal_end_time',
                    'cal_logs__cal_user_id',

    ]
    ordering_fields = ['cal_name',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = CalculationApiList.objects.all()
    serializer_class = ListCALAPISerializer
    pagination_class = CustomCALAPIPagination

class UpdateEXTAPIViewSet(viewsets.ModelViewSet):
    queryset = ExternalApiList.objects.all()
    serializer_class = UpdateExternalApiListSerializer


class UpdateCalAPIViewSet(viewsets.ModelViewSet):
    queryset = CalculationApiList.objects.all()
    serializer_class = UpdateCalculationApiListSerializer


class GetInvoiceUrl(APIView):
    def get(self, request):
        dd_id = request.query_params['id']
        order = NewOrder.objects.get(dd_id=dd_id)
        order_id = order.order_id
        order_item_id = order.order_item_id
        file_path = '/buymore2/orders/invoices/' + order_id + '#' + order_item_id + '.pdf'
        access_token = 'd7ElXR2Sr-AAAAAAAAAAC2HC0qc45ss1TYhRYB4Jy6__NJU1jjGiffP7LlP_2rrf'
        dbx = dropbox.Dropbox(access_token)
        link = dbx.files_get_temporary_link(file_path).link
        return Response({
            'link': link
        })

class DownloadMFList(APIView):
    def get(self, request):
        mf_id = request.query_params['mf_id']
        file_path = '/buymore2/orders/manifest/'+'mf_id-'+mf_id+'.pdf'
        link = dbx.files_get_temporary_link(file_path).link
        return Response({
            'link': link
        })



# class DownloadPODList(APIView):
#     def get(self, request):
#         picklist_id = request.query_params['picklist_id']
#         file_path = '/buymore2/orders/PODlist/'+picklist_id+'.pdf'
#         link = dbx.files_get_temporary_link(file_path).link
#         return Response({
#             'link': link
#         })
class CustomOrderForColumnPagination(PageNumberPagination):
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
                    # 'buymore_order_id':'Buymore Order ID',
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
                    'status': "Order Status",
                    'is_canceled':'IS Canceled',
                    'cancel_inward_bin': 'Cancel Inward Bin',
                    'return_request_date':'Return Request Date',
                    'actual_return_date':'Actual Request Date',
                    'case_id':'Case ID',
                    'status_of_case':'Status Of Case',
                    'reimbursement_amount': 'Reimburesement Amount',
                   },
                'sortable': [
                    'buymore_order_id',
                    'dd_id',
                ],

            },
            'results': data
        })
class NewOrdersColumnViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = DynamicFieldsNewOrdersModelSerializer
    pagination_class = CustomOrderForColumnPagination

    def get_queryset(self, *args, **kwargs):
        qs = NewOrder.objects.all()
        query = self.request.GET.get("fields")
        if query:
            return qs
        else:
            return qs


class ReturnColumnViewSet(viewsets.ModelViewSet):
    # queryset = Employee.objects.all()
    serializer_class = DynamicFieldsReturnsModelSerializer
    pagination_class = CustomOrderReturnPagination

    def get_queryset(self, *args, **kwargs):
        qs = NewOrder.objects.all()
        query = self.request.GET.get("fields")
        if query:
            return qs
        else:
            return qs