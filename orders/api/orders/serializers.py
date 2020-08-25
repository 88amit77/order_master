from rest_framework import serializers
from .models import (PODList, ManiFest, NewOrder, Reimburesement, DispatchDetails,
                    FulfilledReturn, RefundImageTable, Reimbursement,TestingNames,TestingStatus,
                     ExternalApiList,ExternalApiLog,CalculationApiList,CalculationApiLog)




class NewOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrder
        fields = '__all__'

class DispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = '__all__'


class FulfilledReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = FulfilledReturn
        fields = '__all__'


class ReimburesementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimburesement
        fields = '__all__'


class PODListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PODList
        fields = '__all__'


class ManiFestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManiFest
        fields = '__all__'

class RefundImageTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefundImageTable
        fields = '__all__'


#for order view page
class OrderViewDispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ('is_canceled', 'cancel_inward_bin', 'status')


class OrderViewFulfilledReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = FulfilledReturn
        fields = ('return_request_date', 'actual_return_date')


class OrderViewReimburesementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimburesement
        fields = ('case_id', 'status_of_case', 'reimbursement_amount')


class OrderViewNewOrderSerializer(serializers.ModelSerializer):
    dd_dispatchdetailss = OrderViewDispatchDetailsSerializer(many=True)
    dd_fullfilledreturn = OrderViewFulfilledReturnSerializer(many=True)
    dd_reimburesements = OrderViewReimburesementSerializer(many=True)
    class Meta:
        model = NewOrder
        fields = ('dd_id', 'product_id', 'order_id', 'order_item_id', 'order_date',
                  'dispatch_by_date', 'portal_id', 'portal_sku', 'qty', 'selling_price', 'mrp', 'tax_rate', 'warehouse_id',
                  'region', 'payment_method', 'dd_dispatchdetailss', 'dd_fullfilledreturn', 'dd_reimburesements')

#update for view page
class OrderViewUpdateIsCancelBinDispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ('is_canceled',)

class OrderViewUpdateCancelInwarBinDispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ('cancel_inward_bin',)

class updateBinIdSerializer(serializers.Serializer):

    dd_dispatchdetailss = OrderViewUpdateIsCancelBinDispatchDetailsSerializer(many=True)

    class Meta:
        model = NewOrder
        fields = ('dd_dispatchdetailss',)

    def update(self, instance, validated_data):

        dd_dispatchdetailss_data = validated_data.pop('dd_dispatchdetailss')
        dd_id = (instance.dd_dispatchdetailss).all()
        dd_id = list(dd_id)
        instance.save()

        for dd_dispatchdetail_data in dd_dispatchdetailss_data:
            dd_idd = dd_id.pop(0)
            dd_idd.is_canceled = dd_dispatchdetail_data.get('is_canceled', dd_idd.is_canceled)
            dd_idd.save()
        return instance

class updateCancelBinIdSerializer(serializers.Serializer):

    dd_dispatchdetailss = OrderViewUpdateCancelInwarBinDispatchDetailsSerializer(many=True)

    class Meta:
        model = NewOrder
        fields = ('dd_dispatchdetailss',)

    def update(self, instance, validated_data):

        dd_dispatchdetailss_data = validated_data.pop('dd_dispatchdetailss')
        dd_id = (instance.dd_dispatchdetailss).all()
        dd_id = list(dd_id)
        instance.save()

        for dd_dispatchdetail_data in dd_dispatchdetailss_data:
            dd_idd = dd_id.pop(0)
            dd_idd.cancel_inward_bin = dd_dispatchdetail_data.get('cancel_inward_bin', dd_idd.cancel_inward_bin)
            dd_idd.save()
        return instance

#return management PODList page
class ReturnManagementPODListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PODList
        fields = ('pod_id', 'pod_number', 'courier_partner_name', 'warehouse_id', 'pod_image_list', 'total_quantity_received')


#order case status
class NewOrderCaseStatusSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrder
        fields =('dd_id', 'order_id', 'order_item_id', 'qty','product_id')

#for data matching return processing
class SerachReturnProcessingSerializer(serializers.ModelSerializer):
    dd_fullfilledreturn = FulfilledReturnSerializer(many=True)
    class Meta:
        model = NewOrder
        fields = ('dd_id', 'order_id', 'order_item_id', 'qty','product_id', 'dd_fullfilledreturn')


class CreateCaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reimbursement
        fields ='__all__'


class CaseStatusListSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField(method_name='get_data')
    class Meta:
         model = Reimbursement
         #fields =('case_id', 'status_of_case', 'reimbursement_amount', 'quantity', 'dd_id')

         fields = ('rr_id', 'case_id', 'status_of_case', 'reimbursement_amount', 'quantity','dd_id' )



    def get_data(self, obj):

            c = 200
            return c
            #return obj.dd_id.count()

#order manifest page
class DispathSerializer(serializers.ModelSerializer):
    class Meta:
        model =DispatchDetails
        fields =('dipatch_details_id', 'dd_id', 'awb','mf_id',)


class CreateManiFestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManiFest
        fields = '__all__'

class ManifestListSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField(method_name='get_data')
    class Meta:
         model = ManiFest
         fields = ('mf_id', 'courier_partner', 'created_date', 'quantity')

    def get_data(self, obj):

        c = 200
        return c

#order return
class DispatchDetailsSerializer1(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ("cancel_inward_bin", "courier_partner")

class FulfilledReturnSerializer1(serializers.ModelSerializer):
    class Meta:
        model = FulfilledReturn
        fields = ("return_request_date", "actual_return_date", 'return_reason', 'sub_reason', 'awb', 'pod_id', 'return_type')


class RefundImageTableSerializer1(serializers.ModelSerializer):
    class Meta:
        model = RefundImageTable
        fields = ("product_condition", "package_condition", 'image_correctness', 'size_correctness', 'alternate_product_id','image_list')

class OrderReturnSerializer(serializers.Serializer):
    # buymore_order_id = serializers.IntegerField()
    dd_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    order_id = serializers.CharField(max_length=50)
    order_item_id = serializers.CharField(max_length=50)
    order_date = serializers.DateField()
    dispatch_by_date = serializers.DateField()
    # portal_sku = serializers.CharField(max_length=30)
    warehouse_id = serializers.IntegerField()

    dd_dispatchdetailss = DispatchDetailsSerializer1(many=True)
    dd_fullfilledreturn = FulfilledReturnSerializer1(many=True)
    dd_refundimagetable = RefundImageTableSerializer1(many=True)


    def update(self, instance, validated_data):
        dd_dispatchdetailss_data = validated_data.pop('dd_dispatchdetailss')
        dd_id = (instance.dd_dispatchdetailss).all()
        dd_id1 = list(dd_id)

        dd_fullfilledreturn_data = validated_data.pop('dd_fullfilledreturn')
        dd_id = (instance.dd_fullfilledreturn).all()
        dd_id2 = list(dd_id)

        dd_refundimagetable_data = validated_data.pop('dd_refundimagetable')
        dd_id = (instance.dd_refundimagetable).all()
        dd_id = list(dd_id)

        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.order_id = validated_data.get('order_id', instance.order_id)
        instance.order_item_id = validated_data.get('order_item_id', instance.order_item_id)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.dispatch_by_date = validated_data.get('dispatch_by_date', instance.dispatch_by_date)
        #instance.portal_sku = validated_data.get('portal_sku', instance.portal_sku)
        instance.warehouse_id = validated_data.get('warehouse_id', instance.warehouse_id)
        instance.save()

        for dd_dispatchdetail_data in dd_dispatchdetailss_data:
            dd_idd = dd_id1.pop(0)
            dd_idd.cancel_inward_bin = dd_dispatchdetail_data.get('cancel_inward_bin', dd_idd.cancel_inward_bin)
            dd_idd.courier_partner = dd_dispatchdetail_data.get('courier_partner', dd_idd.courier_partner)
            dd_idd.save()

        for dd_fullfilledreturnn_data in dd_fullfilledreturn_data:
            dd_idd = dd_id2.pop(0)
            dd_idd.return_request_date = dd_fullfilledreturnn_data.get('return_request_date', dd_idd.return_request_date)
            dd_idd.actual_return_date = dd_fullfilledreturnn_data.get('actual_return_date', dd_idd.actual_return_date)
            dd_idd.return_reason = dd_fullfilledreturnn_data.get('return_reason', dd_idd.return_reason)
            dd_idd.sub_reason = dd_fullfilledreturnn_data.get('sub_reason', dd_idd.sub_reason)
            dd_idd.awb = dd_fullfilledreturnn_data.get('awb', dd_idd.awb)
            dd_idd.pod_id = dd_fullfilledreturnn_data.get('pod_id', dd_idd.pod_id)
            dd_idd.return_type = dd_fullfilledreturnn_data.get('return_type', dd_idd.return_type)
            dd_idd.save()

        for dd_refundimagetablee_data in dd_refundimagetable_data:
            dd_idd = dd_id.pop(0)
            dd_idd.product_condition = dd_refundimagetablee_data.get('product_condition', dd_idd.product_condition)
            dd_idd.package_condition = dd_refundimagetablee_data.get('package_condition', dd_idd.package_condition)
            dd_idd.image_correctness = dd_refundimagetablee_data.get('image_correctness', dd_idd.image_correctness)
            dd_idd.size_correctness = dd_refundimagetablee_data.get('size_correctness', dd_idd.size_correctness)
            dd_idd.alternate_product_id = dd_refundimagetablee_data.get('alternate_product_id', dd_idd.alternate_product_id)

            dd_idd.image_list = dd_refundimagetablee_data.get('image_list', dd_idd.image_list)
            dd_idd.save()
        return instance

#order return process page
class OrderReturnProcessSerializers(serializers.ModelSerializer):
    class Meta:
        model = RefundImageTable
        fields = ("dd_id", "image_list", 'tracking_id', 'package_condition', 'product_condition','return_category','created_at',
                  'is_barcode_required', 'image_correctness', 'size_correctness', 'alternate_product_id', 'return_notes')

#for API testing
class TestingNamesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestingNames
        fields = '__all__'

class TestingStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestingStatus
        fields = '__all__'

####for master search testing
class ForMasterSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingStatus
        fields = "__all__"

class MasterSearchTestingSerializer(serializers.ModelSerializer):
    testing_statuss = ForMasterSearchSerializer(many=True)

    class Meta:
        model = TestingNames
        fields = ('tn_id','tn_name', 'tn_type', 'average_time', 'tn_cron_code', 'testing_statuss')

class ListTestingNames1Serializer(serializers.ModelSerializer):
    testing_statuss = TestingStatusSerializer(many=True)
    class Meta:
        model = TestingNames
        fields = ('tn_id', 'tn_name', 'average_time', 'tn_cron_code', 'tn_type', 'testing_statuss')

class TestUpdateSerializer(serializers.Serializer):
    tn_id = serializers.IntegerField()
    tn_name = serializers.CharField(max_length=50)
    average_time = serializers.FloatField()

    testing_statuss = TestingStatusSerializer(many=True)

    def update(self, instance, validated_data):
        testing_statuss_data = validated_data.pop('testing_statuss')
        dd_id = (instance.testing_statuss).all()
        dd_id1 = list(dd_id)


        #instance.tn_id = validated_data.get('tn_id', instance.tn_id)
        instance.tn_name = validated_data.get('tn_name', instance.tn_name)
        instance.average_time = validated_data.get('average_time', instance.average_time)
        instance.save()

        for testing_statuss_data1 in testing_statuss_data:
            dd_idd = dd_id1.pop(0)
            dd_idd.ts_starttime = testing_statuss_data1.get('ts_starttime', dd_idd.ts_starttime)
            dd_idd.ts_stoptime = testing_statuss_data1.get('ts_stoptime', dd_idd.ts_stoptime)
            dd_idd.ts_status = testing_statuss_data1.get('ts_status', dd_idd.ts_status)

            dd_idd.save()

        return instance


#API log page
class ExternalApiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalApiList
        fields = '__all__'


class ExternalApiLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalApiLog
        fields = '__all__'


class CalculationApiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationApiList
        fields = '__all__'


class CalculationApiLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationApiLog
        fields = '__all__'


class ListEXTAPISerializer(serializers.ModelSerializer):
    ext_log = ExternalApiLogSerializer(many=True)
    class Meta:
        model = ExternalApiList
        fields = ('eal_id', 'eal_name', 'eal_portal_id', 'eal_account_id', 'eal_average_time', 'eal_cron_code', 'ext_log')


class ListCALAPISerializer(serializers.ModelSerializer):
    cal_logs = CalculationApiLogSerializer(many=True)
    class Meta:
        model = CalculationApiList
        fields = ('cal_id', 'cal_name', 'cal_table_id', 'cal_average_time', 'cal_cron_code', 'cal_logs')


class UpdateExternalApiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalApiList
        fields = ('eal_id','eal_cron_code')


class UpdateCalculationApiListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationApiList
        fields = ('cal_id', 'cal_cron_code')

##for new order column select
class DynamicFieldsNewOrdersModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsNewOrdersModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    dd_dispatchdetailss = OrderViewDispatchDetailsSerializer(many=True)
    dd_fullfilledreturn = OrderViewFulfilledReturnSerializer(many=True)
    dd_reimburesements = OrderViewReimburesementSerializer(many=True)




    class Meta:
        model = NewOrder
        fields = ('dd_id', 'product_id', 'order_id', 'order_item_id', 'order_date',
                  'dispatch_by_date', 'portal_id', 'portal_sku', 'qty', 'selling_price', 'mrp', 'tax_rate',
                  'warehouse_id','region', 'payment_method', 'dd_dispatchdetailss', 'dd_fullfilledreturn', 'dd_reimburesements')

##for return view column select
class DynamicFieldsReturnsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('fields', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(DynamicFieldsReturnsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    dd_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    order_id = serializers.CharField(max_length=50)
    order_item_id = serializers.CharField(max_length=50)
    order_date = serializers.DateField()
    dispatch_by_date = serializers.DateField()
    # portal_sku = serializers.CharField(max_length=30)
    warehouse_id = serializers.IntegerField()

    dd_dispatchdetailss = DispatchDetailsSerializer1(many=True)
    dd_fullfilledreturn = FulfilledReturnSerializer1(many=True)
    dd_refundimagetable = RefundImageTableSerializer1(many=True)

    class Meta:
        model = NewOrder
        fields = ('dd_id', 'product_id', 'order_id', 'order_item_id', 'order_date',
                  'dispatch_by_date', 'warehouse_id','dd_dispatchdetailss', 'dd_fullfilledreturn',
                  'dd_refundimagetable')
