from django.db import models

class ManiFest(models.Model):
    mf_id = models.AutoField(primary_key=True)
    courier_partner = models.CharField(max_length=50)
    mf_sheet = models.URLField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    # dipatch_details_id = models.ManyToManyField(DispatchDetails)
    def __str__(self):
        return str(self.mf_id)


class NewOrder(models.Model):
   # buymore_order_id = models.AutoField(primary_key=True)
    dd_id = models.AutoField(primary_key=True)
    buymore_sku = models.CharField(max_length=20)
    product_id = models.IntegerField()
    order_id = models.CharField(max_length=20)
    order_item_id = models.CharField(max_length=20)
    order_date = models.DateField()
    dispatch_by_date = models.DateField()
    portal_id = models.IntegerField()
    portal_sku = models.CharField(max_length=30)
    qty = models.IntegerField()
    selling_price = models.FloatField()
    mrp = models.FloatField()
    tax_rate = models.FloatField()
    warehouse_id = models.IntegerField()
    region = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=30)

    def __str__(self):
        return str(self.dd_id)


class DispatchDetails(models.Model):
    dipatch_details_id = models.AutoField(primary_key=True)
    dd_id = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='dd_dispatchdetailss', null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pincode = models.IntegerField()
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    email_id = models.EmailField()
    phone = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    l_b_h_w = models.CharField(max_length=50)
    bin_Id = models.IntegerField()
    picklist_id = models.IntegerField()
    is_mark_placed = models.BooleanField(default=False)
    have_invoice_file = models.BooleanField(default=False)
    packing_status = models.BooleanField(default=False)
    is_dispatch = models.BooleanField(default=False)
    dispatch_confirmed = models.BooleanField(default=False)
    mf_id = models.ForeignKey(ManiFest, on_delete=models.CASCADE, related_name='mf_dispatchdetailss', null=True, blank=True)
    is_shipment_create = models.BooleanField(default=False)
    awb = models.CharField(max_length=30, null=True, blank=True)
    courier_partner = models.CharField(max_length=30)
    shipment_id = models.IntegerField()
    is_canceled = models.BooleanField(default=False)
    cancel_inward_bin = models.CharField(max_length=30)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return self.awb

# class ManiFest(models.Model):
#     mf_id = models.AutoField(primary_key=True)
#     courier_partner = models.CharField(max_length=20)
#     mf_sheet = models.URLField(null=True, blank=True)
#     created_date = models.DateField(auto_now_add=True)
#     dipatch_details_id = models.ManyToManyField(DispatchDetails)
#     def __str__(self):
#         return str(self.mf_id)


class Reimburesement(models.Model):
    rr_id = models.AutoField(primary_key=True)
    dd_id = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='dd_reimburesements', null=True, blank=True)
    case_id = models.CharField(max_length=20)
    status_of_case = models.CharField(max_length=20)
    case_content = models.CharField(max_length=20)
    case_reply = models.CharField(max_length=20)
    reimbursement_amount = models.FloatField()


class Reimbursement(models.Model):
    rr_id = models.AutoField(primary_key=True)
    dd_id = models.ManyToManyField(NewOrder, related_name='reimbursements', null=True, blank=True)
    case_id = models.CharField(max_length=20)
    status_of_case = models.CharField(max_length=20)
    case_content = models.CharField(max_length=20)
    case_reply = models.CharField(max_length=20)
    reimbursement_amount = models.FloatField()

class PODList(models.Model):
    pod_id = models.AutoField(primary_key=True)
    pod_number = models.CharField(max_length=20)
    courier_partner_name = models.CharField(max_length=30)
    pod_image_list = models.URLField(null=True, blank=True)
    total_quantity_received = models.IntegerField()
    processed_quantity = models.IntegerField(null=True, blank=True)
    warehouse_id = models.IntegerField(null=True, blank=True)
    courier_received_date = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.pod_id)



class FulfilledReturn(models.Model):
     fr_id = models.AutoField(primary_key=True)
     dd_id = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='dd_fullfilledreturn', null=True, blank=True)
     return_request_date = models.DateField()
     actual_return_date = models.DateField(blank=True, null=True,)
     destination_warehouse_id = models.IntegerField()
     return_reason = models.CharField(max_length=70)
     sub_reason = models.CharField(max_length=50)
     awb  = models.CharField(max_length=40)
     pod_id  = models.ForeignKey(PODList, on_delete=models.CASCADE, related_name='pod_fullfilledreturn', null=True, blank=True)
     return_type  = models.CharField(max_length=20)


class RefundImageTable(models.Model):
    dd_id = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='dd_refundimagetable', null=True,
                              blank=True)
    image_list = models.FileField(blank=True, null=True,)
    return_category = models.CharField(max_length=50, blank=True, null=True)
    return_notes = models.CharField(max_length=100, blank=True, null=True)
    tracking_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, )
    processing_date = models.DateTimeField(blank=True, null=True, )
    return_type = models.CharField(max_length=50, blank=True, null=True)
    package_condition = models.CharField(max_length=50)
    is_barcode_required = models.BooleanField(default=False, blank=True, null=True)
    product_condition = models.CharField(max_length=50)
    image_correctness = models.BooleanField(default=False)
    size_correctness = models.BooleanField(default=False)
    alternate_product_id = models.PositiveIntegerField(blank=True, null=True, )
    sellable = models.BooleanField(default=False, blank=True, null=True)
    pod_id = models.ForeignKey(PODList, on_delete=models.CASCADE, related_name='pod_refundimagetable', null=True,
                               blank=True)


class TestingNames(models.Model):
    tn_id = models.AutoField(primary_key=True)
    tn_name = models.CharField(max_length=50)
    average_time = models.FloatField(default=0.0)
    tn_cron_code = models.CharField(max_length=50,null=True, blank=True)
    tn_type = models.PositiveIntegerField()

    def __str__(self):
        return str(self.tn_type)


class TestingStatus(models.Model):
    ts_id = models.AutoField(primary_key=True)
    tn_id = models.ForeignKey(TestingNames, related_name='testing_statuss', on_delete=models.CASCADE, default=None,
                              unique=False)
    ts_starttime = models.DateTimeField(auto_now_add=True)
    ts_startfile = models.URLField(null=True, blank=True)
    ts_stoptime = models.DateTimeField(auto_now_add=True)
    ts_stopfilelog = models.URLField(null=True, blank=True)
    ts_status = models.CharField(max_length=100,null=True, blank=True)


class ExternalApiList(models.Model):

    eal_id = models.AutoField(primary_key=True)
    eal_name = models.CharField(max_length=50)
    eal_portal_id = models.PositiveIntegerField(null=True, blank=True)
    eal_account_id = models.PositiveIntegerField(null=True, blank=True)
    eal_average_time = models.FloatField(default=0.0)
    eal_cron_code = models.CharField(max_length=50,null=True, blank=True)

class ExternalApiLog(models.Model):

    external_api_log_id = models.AutoField(primary_key=True)
    eal_id = models.ForeignKey(ExternalApiList, on_delete=models.CASCADE, related_name='ext_log', null=True, blank=True)
    eal_start_time = models.DateTimeField(auto_now_add=True)
    eal_end_time = models.DateTimeField(null=True, blank=True)
    eal_log = models.URLField(null=True, blank=True)
    eal_status = models.PositiveIntegerField(null=True, blank=True)
    eal_input_file = models.URLField(null=True, blank=True)
    eal_output_log = models.URLField(null=True, blank=True)
    eal_user_id = models.PositiveIntegerField(null=True, blank=True)

class CalculationApiList(models.Model):

    cal_id = models.AutoField(primary_key=True)
    cal_name = models.CharField(max_length=50)
    cal_table_id = models.CharField(max_length=50,null=True, blank=True)
    cal_average_time= models.FloatField(default=0.0)
    cal_cron_code = models.CharField(max_length=50,null=True, blank=True)

class CalculationApiLog(models.Model):
    calculation_api_log_id = models.AutoField(primary_key=True)
    cal_id = models.ForeignKey(CalculationApiList, on_delete=models.CASCADE, related_name='cal_logs', null=True, blank=True)
    cal_start_time = models.DateTimeField(auto_now_add=True)
    cal_end_time = models.DateTimeField(null=True, blank=True)
    cal_log = models.URLField(null=True, blank=True)
    cal_status = models.PositiveIntegerField(null=True, blank=True)
    cal_input_file = models.URLField(null=True, blank=True)
    cal_outputfile = models.URLField(null=True, blank=True)
    cal_user_id = models.PositiveIntegerField(null=True, blank=True)