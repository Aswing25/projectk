from django.db import models

# Create your models here.
class registerdb(models.Model):
    username = models.CharField(max_length=20,blank=True,null=True)
    rpassword = models.CharField(max_length=20,blank=True,null=True)