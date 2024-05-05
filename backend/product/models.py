from django.db import models

# Create your models here.
class UOM(models.Model):
      uom_name = models.CharField(max_length=100)
      
      def __str__(self):
            return f"{self.uom_name}"

class Product(models.Model):
      name = models.CharField(max_length=100)
      uom_id = models.ForeignKey(UOM, on_delete=models.CASCADE)
      price_per_unit = models.FloatField()
      
      def __str__(self) -> str:
            return f"{self.name}"

class Order(models.Model):
      customer_name = models.CharField(max_length=100)
      total = models.FloatField()
      datetime = models.DateTimeField(auto_now_add=True)
      
      def __str__(self) -> str:
            return f"{self.datetime}-{self.customer_name}"
      
class Order_details(models.Model):
      order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
      product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.FloatField()
      total_price = models.FloatField()