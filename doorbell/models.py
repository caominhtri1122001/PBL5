from django.db import models

# Create your models here.
class GuestImage(models.Model):
    name = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField()
    gender = models.CharField(max_length=20, null=True, blank=True, default="None")
    date = models.CharField(max_length=50,null=True,blank=True)
    time = models.CharField(max_length=50,null=True,blank=True)