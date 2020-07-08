from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .orders import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = DefaultRouter()
schema_view = get_schema_view(openapi.Info(
      title="Orders API",
      default_version='v1',
      description="Test description",
   ), public=True, permission_classes=(permissions.AllowAny,))
#schema_view = get_swagger_view(title='Microservice API')


#each table Order APIs
router.register('order/new_order', views.NewOrderViewSet, basename="new_order")
router.register('order/dispatch_details', views.DispatchDetailsViewSet, basename="dispatch_details")
router.register('order/reimburesement', views.ReimburesementViewSet, basename="reimburesement")
router.register('order/fulfilled_return', views.FulfilledReturnViewSet, basename="fulfilled_return")
router.register('order/pod_list', views.PODListViewSet, basename="pod_list")
router.register('order/mani_fest', views.ManiFestViewSet, basename="mani_fest")
router.register('order/refund_image_table', views.RefundImageTableViewSet, basename="refund_image_table")
#for oreder view
router.register('order/order_view', views.orderviewViewSet, basename="order_view")
router.register('order/list_order_view', views.ListorderViewSet, basename="list_order_view")
router.register('order/update_bin_id', views.updateBinIdViewSet, basename="update_bin_id")
router.register('order/update_cancel_bin_id', views.updateCancelBinIdViewSet, basename="update_cancel_bin_id")

#return management POD list page
router.register('order/create_pod_list', views.CreateRMPODlistViewSet, basename="create_pod_list")
router.register('order/list_pod_list', views.ListRMPODlistViewSet, basename="list_pod_list")

#order case status
router.register('order/create_case_status', views.CreateordercasestatusViewSet, basename="create_case_status")
router.register('order/list_case_status', views.ListordercasestatusViewSet, basename="list_case_status")

# order mani fest
router.register('order/create_manifest', views.CreateManiFestViewSet, basename="create_manifest")
router.register('order/list_manifest', views.ListManiFestViewSet, basename="list_manifest")
#for separate  date filter
router.register(r'order/^order_date_filter',views.OrderDateFilterViewSet,basename='order_date_filter')
router.register(r'order/^dispatch_by_date_filter',views.DispatchByDateFilterViewSet,basename='dispatch_by_date_filter')

#order_return
router.register('order/list_order_return', views.ListOrderReturnViewSet, basename="list_order_return")
router.register('order/update_search_order_return', views.updateIdViewSet, basename='update_search_order_return')
#order return process page
router.register('order/create_order_return_process', views.OrderReturnProcessViewSet, basename='create_order_return_process')
router.register('order/search_fulfilled_return', views.SearchFulfilledReturnViewSet, basename="search_fulfilled_return")
router.register('order/Serach_Return_Processing', views.SerachReturnProcessingViewSet, basename="Serach_Return_Processing")
#ERP testing
router.register('order/testing_names', views.TestingNamesViewSet, basename="testing_names")
router.register('order/testing_status', views.TestingStatusViewSet, basename="testing_status")
router.register('order/list_testing', views.ListAssignRulesViewSet, basename="list_testing")
router.register('order/search_testing_Tn_Type', views.SearchTestViewSet, basename="search_testing")
router.register('order/update_testing', views.UpdateTestViewSet, basename="update_testing")
#ERP testing APILOG page API
router.register(r'order/external_api_list', views.ExternalApiListViewSet, basename='external_api_list')
router.register(r'order/external_api_log', views.ExternalApiLogViewSet, basename='external_api_log')
router.register(r'order/cal_api_list', views.CalculationApiListViewSet, basename='cal_api_list')
router.register(r'order/cal_api_log', views.CalculationApiLogViewSet, basename='cal_api_log')

router.register(r'order/list_ext_api', views.ListEXTAPIViewSet, basename='list_ext_api')
router.register(r'order/list_cal_api', views.ListCALAPIViewSet, basename='list_cal_api')
router.register(r'order/search_ext_api', views.SearchEXTAPIViewSet, basename='search_ext_api')
router.register(r'order/search_cal_api', views.SearchCalAPIViewSet, basename='search_cal_api')
router.register(r'order/update_ext_api', views.UpdateEXTAPIViewSet, basename='update_ext_api')
router.register(r'order/update_cal_api', views.UpdateCalAPIViewSet, basename='update_cal_api')


urlpatterns = [
    path('', include(router.urls)),
    path('order/orders_docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('order/order_view_search/', views.OrderViewSearchAPIView.as_view()),
    path('order/list_pod_list_search/', views.SearchListRMPODlistViewSet.as_view()),
    path('order/list_pod_Warehousewise_search/', views.SearchListRMPODlistWarehouseViewSet.as_view()),
    path('order/case_status_data_match_search/', views.NewOrderCaseStatusSearchViewSet.as_view()),
    path('order/list_case_status_search/', views.SearchListordercasestatusViewSet.as_view()),
    path('order/manifest_data_match_search/', views.NewOrderManifestSearchViewSet.as_view()),
    path('order/list_manifest_search/', views.SearchListManiFestViewSet.as_view()),
    path('order/testing_master_search/', views.SearchTestViewSet22.as_view()),
    path('order/order_id_search/', views.SearchOrderIDViewSet.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
