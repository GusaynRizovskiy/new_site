from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)
