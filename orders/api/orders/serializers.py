from rest_framework import serializers
from .models import PODList, ManiFest, NewOrder, Reimburesement, DispatchDetails, FulfilledReturn, RefundImageTable




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
#worked perfectly
# class updateBinIdSerializer(serializers.Serializer):
#
#     dd_dispatchdetailss = DispatchDetailsSerializer(many=True)
#
#     class Meta:
#         model = NewOrder
#         fields = ('buymore_order_id', 'dd_dispatchdetailss')
#
#     def update(self, instance, validated_data):
#
#         dd_dispatchdetailss_data = validated_data.pop('dd_dispatchdetailss')
#         dd_id = (instance.dd_dispatchdetailss).all()
#         dd_id = list(dd_id)
#         instance.save()
#
#         for dd_dispatchdetail_data in dd_dispatchdetailss_data:
#             dd_idd = dd_id.pop(0)
#             dd_idd.is_canceled = dd_dispatchdetail_data.get('is_canceled', dd_idd.is_canceled)
#             dd_idd.save()
#         return instance
class OrderViewUpdateCancelInwarBinDispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ('is_canceled',)

class OrderViewUpdateISCancelDispatchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispatchDetails
        fields = ('cancel_inward_bin',)

class updateBinIdSerializer(serializers.Serializer):

    dd_dispatchdetailss = OrderViewUpdateISCancelDispatchDetailsSerializer(many=True)

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

    dd_dispatchdetailss = OrderViewUpdateISCancelDispatchDetailsSerializer(many=True)

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
