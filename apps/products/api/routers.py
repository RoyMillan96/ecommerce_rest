from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.general_views import (
    MeasureUnitViewSet, IndicatorViewSet, CategoryProductViewSet
)
from apps.products.api.viewsets.product_viewsets import ProductViewSet

router = DefaultRouter()

router.register(r'product', ProductViewSet, basename='products')
router.register(r'measure-unit', MeasureUnitViewSet, basename='meausre_unit')
router.register(r'indicators', IndicatorViewSet, basename='indicators')
router.register(r'category-products', CategoryProductViewSet, basename='category_products')
urlpatterns = router.urls