from django.db import models

# Create your models here.

#モデルクラスを継承
class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()