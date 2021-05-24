from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    des=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name

class Order_detail(models.Model):
    state_region=((0,'Uttar Pradesh'),(1,'Madhya Pradesh'),(2,'Jharkhand'),(3,"Bihar"))
    Payment_mode=((0,"cash on delivery"),(1,"online payment"))
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    pin=models.CharField(max_length=10)
    state=models.CharField(max_length=20,choices=state_region,default=0)
    radio=models.CharField(max_length=20,choices=Payment_mode,default=0)
    date = models.DateField()
