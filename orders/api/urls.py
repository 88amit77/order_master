from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
schema_view = get_swagger_view(title='Microservice API')
urlpatterns = [
    path('', include(router.urls)),
    path("docs/", schema_view),
]
