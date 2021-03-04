from django.db import models
from rest_framework import serializers

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductSKU = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.FloatField()
    ProductWeight = models.FloatField()
    ProductCartDesc = models.CharField(max_length=250)
    ProductShortDesc = models.CharField(max_length=1000)
    ProductLongDesc = models.TextField()
    ProductThumb = models.CharField(max_length=100, blank=True)
    ProductImage = models.CharField(max_length=100, blank=True)
    ProductCategoryID = models.IntegerField()
    ProductUpdateDate = models.DateTimeField()
    ProductStock = models.FloatField()
    ProductLive = models.SmallIntegerField()
    ProductUnlimited = models.SmallIntegerField()
    ProductLocation = models.CharField(max_length=250)
    def __str__(self):
        return '[{}] {}'.format(self.ProductID, self.ProductName)

class Category(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=50)
    class Meta:
        db_table = 'productcategories'
    
    