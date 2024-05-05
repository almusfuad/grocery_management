
from django.contrib import admin
from .models import UOM, Product, Order, Order_details


# Register your models here.
admin.site.register(UOM)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Order_details)