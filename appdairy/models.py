from django.db import models

# Create your models here.
#seller side data
class User(models.Model):
    Fname=models.CharField(max_length=150,default="asd#45")
    Lname=models.CharField(max_length=255,default="lname")
    Email=models.EmailField(unique=True)
    Mobile=models.IntegerField(default="456")
    Address=models.CharField(max_length=255,default="address")
    Password=models.CharField(max_length=255,default="password")
    OTP=models.IntegerField(default=000000)
    def __str__(self):
        return self.Lname

class Category(models.Model):
    pcategory=models.CharField(max_length=200,default="product category")
    
    def __str__(self):
        return self.pcategory

class Seller(models.Model):
    Fname=models.CharField(max_length=150,default="asd#45")
    Lname=models.CharField(max_length=255,default="lname")
    Email=models.EmailField(unique=True)
    Mobile=models.IntegerField(default="456")
    Address=models.CharField(max_length=255,default="address")
    Password=models.CharField(max_length=255,default="password")
    OTP=models.IntegerField(default=000000)
    def __str__(self):
        return self.Lname

class Productss(models.Model):
    sellerid=models.ForeignKey(Seller, on_delete=models.CASCADE,default=True)
    Pro_name=models.CharField(max_length=250,default="proname")
    Pro_image=models.ImageField(upload_to="productimage/",default="xyz.jpg")
    Pro_weight=models.IntegerField(default="125pabc")
    Pro_weightCat=models.CharField(max_length=100,default="abc")
    Pro_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    Pro_price=models.FloatField()

    def __str__(self):
        return self.Pro_name



class Carts(models.Model):

    product= models.ForeignKey(Productss, on_delete=models.CASCADE,default=True)
    Userid= models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    Quantity= models.IntegerField(default="1")
    Total= models.IntegerField(default="500")

