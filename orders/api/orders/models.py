from django.db import models




class NewOrder(models.Model):
    buymore_order_id = models.AutoField(primary_key=True)
    dd_id = models.IntegerField()
    product_id = models.IntegerField()
    order_id = models.IntegerField()
    order_item_id = models.IntegerField()
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
    mf_id = models.IntegerField(null=True, blank=True)
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

class ManiFest(models.Model):
    mf_id = models.AutoField(primary_key=True)
    courier_partner = models.CharField(max_length=20)
    mf_sheet = models.URLField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    awb = models.ManyToManyField(DispatchDetails)
    def __str__(self):
        return str(self.mf_id)


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

      dd_id = models.ForeignKey(NewOrder, on_delete=models.CASCADE, related_name='dd_refundimagetable', null=True, blank=True)
      image_list = models.URLField(blank=True, null=True)
      return_category = models.CharField(max_length=50)
      return_notes = models.CharField(max_length=50)
      tracking_id = models.PositiveIntegerField()
      created_at = models.DateTimeField()
      updated_at = models.DateTimeField(blank=True, null=True,)
      processing_date = models.DateTimeField(blank=True, null=True,)
      return_type = models.CharField(max_length=50)
      package_condition = models.CharField(max_length=50,blank=True, null=True)
      is_barcode_required = models.BooleanField(default=False)
      product_condition = models.CharField(max_length=50, blank=True, null=True)
      image_correctness = models.BooleanField(default=False, blank=True, null=True)
      size_correctness = models.BooleanField(default=False)
      alternate_product_id = models.PositiveIntegerField(blank=True, null=True,)
      sellable = models.BooleanField(default=False)
      pod_id = models.ForeignKey(PODList, on_delete=models.CASCADE, related_name='pod_refundimagetable', null=True, blank=True)