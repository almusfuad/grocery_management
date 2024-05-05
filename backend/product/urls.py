from django.urls import path

from .views import create_uom, add_product, show_all_product, delete_product, create_order, order_details, show_order

urlpatterns = [
      path('create_uom/', create_uom, name='create_uom'),
      path('add_product/', add_product, name='add_product'),
      path('show_all_product/', show_all_product, name='show_all_product'),
      path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
      path('create_order/', create_order, name='create_order'),
      path('order_details/', order_details, name='order_details'),
      path('show_order/', show_order, name='show_order')
]