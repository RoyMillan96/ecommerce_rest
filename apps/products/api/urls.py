from django.urls import path

from apps.products.api.viewsets.general_views import (
    MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
)
from apps.products.api.viewsets.product_views import ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_product/', CategoryProductListAPIView.as_view(), name = 'category_product'),
    path('product/list/', ProductListAPIView.as_view(), name = 'product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name = 'product_create'),
]