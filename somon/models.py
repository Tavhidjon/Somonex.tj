from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



class Category(models.Model):
    name=models.CharField( max_length=50)
    def __str__(self):
        return self.name



class Product(models.Model):
    p_name=models.CharField( max_length=150)
    price=models.IntegerField()
    is_active=models.BooleanField(default=True)
    added_at=models.DateTimeField( auto_now=True)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.price
    
class Order(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    custom_id=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date=models.DateTimeField( auto_now=True)
    is_paid=models.BooleanField(default=False)
    def __str__(self):
        return self.order_date
    






