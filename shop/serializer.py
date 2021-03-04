from django.db import models
from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        # fields = ['ProductID', 'ProductSKU', 'ProductName', 'ProductPrice', 'ProductWeight', 'ProductCartDesc', 'ProductShortDesc', 'ProductLongDesc', 'ProductThumb', 'ProductThumb',
        #           'ProductImage', 'ProductCategoryID', 'ProductUpdateDate', 'ProductStock', 'ProductLive', 'ProductUnlimited', 'ProductLocation']

        
