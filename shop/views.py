from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Products, Category
from .serializer import ProductsSerializer

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, './index.html')

@api_view(['GET'])
def get_all_products(request):
    products = Products.objects.all()
    serializer_class = ProductsSerializer(products, many=True)
    return Response(serializer_class.data)
    # context = {'products': products}
    
    # return render(request, './products.html', context)

def get_product_detail(request, name, category):
    category = Category.objects.filter(CategoryName=category).first()
    if category is None:
        products = None
    else:
        category_id = category.CategoryID
        products = Products.objects.filter(ProductName=name, ProductCategoryID=category_id)

    context = {'products': products}
    return render(request, './details.html', context)

class ProductView(APIView):
    # model = Products
    template_name = 'detail.html'
    queryset = Products.objects.all()
    pk_url_kwargs = 'product_id' 
    
    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        return queryset.filter(ProductID=pk).first()
    
    def get(self, request, *args, **kwargs):
        product = self.get_object()
        context = {'product': product}
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
        # return Response(serializer)
        # return render(request, self.template_name, context)