from django.db import models

# Create your models here
class employedb(models.Model):
    ename=models.CharField(max_length=50,blank=True,null=True)
    eage=models.IntegerField(blank=True,null=True)
    mobile=models.IntegerField(blank=True,null=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    company=models.CharField(max_length=50,blank=True,null=True)
    salary=models.IntegerField(blank=True,null=True)
    address=models.CharField(max_length=50,null=True,blank=True)

class studentdb(models.Model):
    sfname=models.CharField(max_length=50,blank=True,null=True)
    slname=models.CharField(max_length=50,blank=True,null=True)
    semail=models.CharField(max_length=50,blank=True,null=True)


class categorydb(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    Cdes=models.CharField(max_length=50,blank=True,null=True)
    categoryimg=models.ImageField(upload_to="category",null=True,blank=True)
    cprice=models.IntegerField(null=True,blank=True)

class productdb(models.Model):
    catname= models.CharField(max_length=100,null=True,blank=True)
    productname = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    productimage = models.ImageField(upload_to="products",null=True,blank=True)