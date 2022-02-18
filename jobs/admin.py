from django.contrib import admin
from jobs.models import Contact,Orderdetail,User,Product_detail,Categorie
# Register your models here
class Admin_Product(admin.ModelAdmin):
    list_display=['id','product_id','name','price','category']
class Admin_Categorie(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Contact)
admin.site.register(Orderdetail)
admin.site.register(User)
admin.site.register(Product_detail,Admin_Product)
admin.site.register(Categorie,Admin_Categorie)