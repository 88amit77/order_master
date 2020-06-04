from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
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


