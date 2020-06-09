from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from .orders import views
from django.urls import path, include

router = DefaultRouter()
schema_view = get_swagger_view(title='Microservice API')


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

urlpatterns = [
    path('', include(router.urls)),
    path("docs/", schema_view),
    path('order_view_search/', views.OrderViewSearchAPIView.as_view()),
    path('list_pod_list_search/', views.SearchListRMPODlistViewSet.as_view()),
    path('list_pod_Warehousewise_search/', views.SearchListRMPODlistWarehouseViewSet.as_view()),
    path('case_status_data_match_search/', views.NewOrderCaseStatusSearchViewSet.as_view()),
    path('list_case_status_search/', views.SearchListordercasestatusViewSet.as_view()),
    path('manifest_data_match_search/', views.NewOrderManifestSearchViewSet.as_view()),
    path('list_manifest_search/', views.SearchListManiFestViewSet.as_view()),
]
