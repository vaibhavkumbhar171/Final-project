from django.contrib import admin
from . import models
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid','c_name','c_addr','c_email','c_phone']
    
admin.site.register(models.Customer)


class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_id','vendor_name','vendor_email','vendor_addr','vgst_no','vphone_no']
    
admin.site.register(models.Vendor)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id','category_name','description']
    
admin.site.register(models.Category)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['offer_id','pro_name','description','discount_percentage','start_date','end_date']
    
admin.site.register(models.Offer)


class GstAdmin(admin.ModelAdmin):
    list_display = ['gst_id','category_gst','igst']
    
admin.site.register(models.Gst)


class productAdmin(admin.ModelAdmin):
    list_display = ['p_id','p_name','vendor','category','product_stock','unit','product_price','reorder','discount','gst_id']
    
admin.site.register(models.Product)


class InvoiceCustomerAdmin(admin.ModelAdmin):
    list_display = ['invoice_id','customer_invoice','gross_cost','tax_amount','discount','netamount','invoice_date']
    
admin.site.register(models.InvoiceCustomer)


class Customer_orderAdmin(admin.ModelAdmin):
    list_display = ['order_id','invoice','product_order','quantity']
    
admin.site.register(models.customer_order)


class VendorInvoice_Admin(admin.ModelAdmin):
    list_display = ['v_invoice','vendorid','invoice_datetime','total_amount']
    
admin.site.register(models.VendorInvoice)


class PurchaseOrder_Admin(admin.ModelAdmin):
    list_display = ['po_id','vendorinvoice','productid','vquantity','vprice','vdatetime']
    
admin.site.register(models.PurchaseOrder)


# class VendorInvoice_Admin(admin.ModelAdmin):
#     list_display = []
    
# admin.site.register()