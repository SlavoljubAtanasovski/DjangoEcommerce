
from . import views
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.get_all_products, name='product-detail'),
    path('search/<str:name>/<str:category>', views.get_product_detail, name='product-detail_i'),
    # path('product/', views.ProductView.as_view(), name='product-detail'),
    path('product/<int:product_id>', views.ProductView.as_view(), name='product-detail-id'),
    path('docs/', get_swagger_view(title="API 문서"), name="swagger"),
]