from rest_framework import serializers
from .models import PODList, ManiFest, NewOrder, Reimburesement, DispatchDetails, FulfilledReturn, RefundImageTable, Reimbursement




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
        fields = ('buymore_order_id', 'dd_id', 'product_id', 'order_id', 'order_item_id', 'order_date',
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
        fields = ('buymore_order_id', 'dd_dispatchdetailss')

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
        fields = ('buymore_order_id', 'dd_dispatchdetailss')

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
        fields = ('pod_id', 'pod_number', 'courier_partner_name', 'pod_image_list', 'total_quantity_received')


#order case status
class NewOrderCaseStatusSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrder
        fields =('buymore_order_id', 'dd_id', 'order_id', 'order_item_id', 'qty')

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
        fields =('dipatch_details_id', 'dd_id', 'awb',)


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