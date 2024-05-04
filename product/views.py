from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# import database models
from .models import UOM, Product, Order, Order_details

# Create your views here.

@api_view(['POST'])
def create_uom(request):
      if request.method == 'POST':
            uom_name = request.data['uom_name']
            uom = UOM.objects.create(uom_name=uom_name)
            return JsonResponse({'message': 'UOM created successfully'})
      
@api_view(['POST'])
def add_product(request):
      if request.method == 'POST':
            name = request.data['name']
            uom_id = request.data['uom_id']
            price_per_unit = request.data['price_per_unit']
            
            try:
                  uom_instance = UOM.objects.get(id=uom_id)
            except UOM.DoesNotExist:
                  return JsonResponse({'message': 'UOM does not exist'}, status=404, content_type='application/json')
            product = Product.objects.create(name = name, uom_id = uom_instance, price_per_unit = price_per_unit)
            return JsonResponse({'message': 'Product created successfully'}, status=200, content_type='application/json')

     
@api_view(['GET'])
def show_all_product(request):
      if request.method == 'GET':
            products = Product.objects.all()
            product_list = []
            for product in products:
                  product_list.append({
                        'name': product.name,
                        'uom_id': product.uom_id.uom_name,
                        'price_per_unit': product.price_per_unit,
                  })
            return JsonResponse({'products': product_list}, status=200, content_type='application/json')
      
      
@api_view(['DELETE'])
def delete_product(request, product_id):
      if request.method == 'DELETE':
            try:
                  product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                  return JsonResponse({'message': 'Product does not exist'}, status=404, content_type='application/json')
            product.delete()
            return JsonResponse({'message': 'Product deleted successfully'}, status=200, content_type='application/json')
      
      
@api_view(['POST'])
def create_order(request):
      customer_name = request.data["customer_name"]
      total = request.data["total"]
      order = Order.objects.create(customer_name=customer_name, total=total)
      return JsonResponse({'message': 'Order created successfully'}, status=200, content_type='application/json')


@api_view(['POST'])
def order_details(request):
      order_id = request.data["order_id"]
      product_id = request.data["product_id"]
      quantity = request.data["quantity"]
      total_price = request.data["total_price"]
      
      try:
            order = Order.objects.get(id=order_id)
      except Order.DoesNotExist:
            return JsonResponse({'message': 'Order does not exist'}, status=404, content_type='application/json')
      
      try:
            product = Product.objects.get(id=product_id)
      except Product.DoesNotExist:
            return JsonResponse({'message': 'Product does not exist'}, status=404, content_type='application/json')
      
      order_detail = Order_details.objects.create(order_id=order, product_id=product, quantity=quantity, total_price=total_price)
      return JsonResponse({'message': 'Order detail created successfully'}, status=200, content_type='application/json')


@api_view(['GET'])
def show_order(request):
      orders = Order.objects.all()
      order_list = []
      for order in orders:
            order_list.append({
                  'customer_name': order.customer_name,
                  'total': order.total,
                  'datetime': order.datetime.date(),
            })