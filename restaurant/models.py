from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    temp=models.CharField(max_length=20)

class MenuItem(models.Model):
    item=models.CharField(max_length=255)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    inventory=models.SmallIntegerField()
    category=models.ForeignKey(Category,on_delete=PROTECT,default=1)
