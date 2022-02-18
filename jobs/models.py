from django.db import models
import uuid,datetime
from django.utils import timezone



# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    des=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name



class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    password=models.CharField(max_length=50)

    def get_customer(username,password):

        try:
            return User.objects.get(username=username,password=password)
        except:
            return False

    def isExists(self):

         if User.objects.filter(username=self.username):
             return True
         else:
             return False

class Categorie(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product_detail(models.Model):
    product_id=models.UUIDField(default=uuid.uuid4)
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    selling_price=models.FloatField(default=0,null=True)
    description=models.CharField(max_length=500,default='')
    image=models.ImageField(upload_to='jobs/static/img/')
    category=models.ForeignKey(Categorie,on_delete=models.CASCADE,default='')
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    date_and_time=models.DateTimeField()




class Orderdetail(models.Model):
    #state_region=((0,'Uttar Pradesh'),(1,'Madhya Pradesh'),(2,'Jharkhand'),(3,"Bihar"))
   # Payment_mode=((0,"cash on delivery"),(1,"online payment"))
    product_id=models.IntegerField(default=0,null=True)
    quantity=models.IntegerField(default=0,null=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    pin=models.CharField(max_length=10)
    state=models.CharField(max_length=20)
    radio=models.CharField(max_length=20)
    username=models.CharField(max_length=100,null=True)
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()
