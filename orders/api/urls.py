from django.conf.urls import url
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .orders import views
from django.urls import path, include

router = DefaultRouter()
schema_view = get_schema_view(openapi.Info(
      title="Orders API",
      default_version='v1',
      description="Test description",
   ), public=True, permission_classes=(permissions.AllowAny,))
#schema_view = get_swagger_view(title='Microservice API')


#each table Order APIs
router.register('new_order', views.NewOrderViewSet, basename="new_order")
router.register('dispatch_details', views.DispatchDetailsViewSet, basename="dispatch_details")
router.register('reimburesement', views.ReimburesementViewSet, basename="reimburesement")
router.register('fulfilled_return', views.FulfilledReturnViewSet, basename="fulfilled_return")
router.register('pod_list', views.PODListViewSet, basename="pod_list")
router.register('mani_fest', views.ManiFestViewSet, basename="mani_fest")
router.register('refund_image_table', views.RefundImageTableViewSet, basename="refund_image_table")
#for oreder view
router.register('order_view', views.orderviewViewSet, basename="order_view")
router.register('list_order_view', views.ListorderViewSet, basename="list_order_view")
router.register('update_bin_id', views.updateBinIdViewSet, basename="update_bin_id")
router.register('update_cancel_bin_id', views.updateCancelBinIdViewSet, basename="update_cancel_bin_id")

#return management POD list page
router.register('create_pod_list', views.CreateRMPODlistViewSet, basename="create_pod_list")
router.register('list_pod_list', views.ListRMPODlistViewSet, basename="list_pod_list")

#order case status
router.register('create_case_status', views.CreateordercasestatusViewSet, basename="create_case_status")
router.register('list_case_status', views.ListordercasestatusViewSet, basename="list_case_status")

# order mani fest
router.register('create_manifest', views.CreateManiFestViewSet, basename="create_manifest")
router.register('list_manifest', views.ListManiFestViewSet, basename="list_manifest")
#for separate  date filter
router.register(r'^order_date_filter',views.OrderDateFilterViewSet,basename='order_date_filter')
router.register(r'^dispatch_by_date_filter',views.DispatchByDateFilterViewSet,basename='dispatch_by_date_filter')

#order_return
router.register('list_order_return', views.ListOrderReturnViewSet, basename="list_order_return")
router.register('update_search_order_return', views.updateIdViewSet, basename='update_search_order_return')
#order return process page
router.register('create_order_return_process', views.OrderReturnProcessViewSet, basename='create_order_return_process')
#ERP testing
router.register('testing_names', views.TestingNamesViewSet, basename="testing_names")
router.register('testing_status', views.TestingStatusViewSet, basename="testing_status")
router.register('list_testing', views.ListAssignRulesViewSet, basename="list_testing")
router.register('search_testing', views.SearchTestViewSet, basename="search_testing")
router.register('update_testing', views.UpdateTestViewSet, basename="update_testing")


urlpatterns = [
    path('', include(router.urls)),
    path("orders_docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('order_view_search/', views.OrderViewSearchAPIView.as_view()),
    path('list_pod_list_search/', views.SearchListRMPODlistViewSet.as_view()),
    path('list_pod_Warehousewise_search/', views.SearchListRMPODlistWarehouseViewSet.as_view()),
    path('case_status_data_match_search/', views.NewOrderCaseStatusSearchViewSet.as_view()),
    path('list_case_status_search/', views.SearchListordercasestatusViewSet.as_view()),
    path('manifest_data_match_search/', views.NewOrderManifestSearchViewSet.as_view()),
    path('list_manifest_search/', views.SearchListManiFestViewSet.as_view()),
    path('order_id_search/', views.SearchOrderIDViewSet.as_view()),
]
