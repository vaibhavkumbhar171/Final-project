from django.db import models

# Create your models here.


class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_addr = models.CharField(max_length=50)
    c_email= models.CharField(max_length=50)
    c_phone = models.BigIntegerField()
    
    def __str__(self):
        return f'{self.c_name}'
    
class Vendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    vendor_email = models.EmailField()
    vendor_addr = models.CharField(max_length=50)
    vgst_no = models.CharField(max_length=50)
    vphone_no = models.BigIntegerField()
    
    def __str__(self):
        return f'{self.vendor_name}'
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.category_name}'
    
    
class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    discount_percentage = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.pro_name}'

class Gst(models.Model):
    gst_id = models.AutoField(primary_key=True)
    category_gst = models.ForeignKey(Category,on_delete=models.CASCADE)
    igst = models.IntegerField()
    
    def __str__(self):
        return f'{self.category_gst}'
    
    
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,models.CASCADE)
    product_stock = models.FloatField()
    unit = models.CharField(max_length=50)
    product_price = models.FloatField()
    reorder_level = models.FloatField()
    discount = models.ForeignKey(Offer, on_delete=models.CASCADE)
    gst_id = models.ForeignKey(Gst,on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.p_name}'

class InvoiceCustomer(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    customer_invoice = models.ForeignKey(Customer,on_delete=models.CASCADE)
    gross_cost = models.FloatField()
    tax_amount = models.IntegerField()
    discount = models.FloatField()
    netamount = models.FloatField()
    invoice_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.invoice_id} {self.netamount} {self.customer_invoice.c_name}'

class customer_order(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(InvoiceCustomer,on_delete=models.CASCADE)
    product_order = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return f'{self.product_order.p_name} ------- {self.quantity} ---- {self.invoice.customer_invoice.c_name} -------- {self.invoice.invoice_id}'
    

class VendorInvoice(models.Model):
    v_invoice = models.AutoField(primary_key=True)
    vendorid = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    invoice_datetime = models.DateTimeField()
    total_amount = models.FloatField()

    def __str__(self):
        return f'{self.v_invoice} ---- {self.total_amount} ---- {self.vendorid.vendor_name}'

class PurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    vendorinvoice = models.ForeignKey(VendorInvoice,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    vquantity = models.FloatField()
    vprice = models.FloatField()
    vdatetime = models.DateTimeField()
    
    def __str__(self):
        return f'{self.productid.p_name} ---- {self.vquantity} ---- {self.productid.vendor.vendor_name}'


class BalanceSheet(models.Model):
    bs_id = models.AutoField(primary_key=True)
    bs_vendor_invoice = models.ForeignKey(VendorInvoice,on_delete=models.CASCADE)
    bs_cinvoice = models.ForeignKey(InvoiceCustomer,on_delete=models.CASCADE)
    light_bill = models.FloatField()
    emp_salary = models.FloatField()
    monthly_rent = models.FloatField()
    miscellaneous = models.FloatField()
    bs_datetime = models.DateTimeField()