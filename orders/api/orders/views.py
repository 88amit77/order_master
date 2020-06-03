from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
import requests
# Create your views here.


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


