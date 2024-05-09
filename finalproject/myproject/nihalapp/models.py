from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class products(models.Model):
    productname = models.CharField(max_length=30)
    image = models.ImageField(upload_to="media")
    productdetail = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    


