from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Product(models.Model):
    class Meta:
        ordering = ["name", "price"]
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(default=0, max_digits=8,decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

class Order(models.Model):
    delivery_address = models.TextField(null=True,blank=True)
    promocode = models.CharField(max_length=20,null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name="orders")