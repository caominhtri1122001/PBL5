from django.db import models

# Create your models here.
class GuestImage(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField()
    date = models.CharField(max_length=100)