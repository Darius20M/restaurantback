from django.urls import re_path
from rest_framework.routers import DefaultRouter

from products.views import ProductViewSet, ProductCategoryViewSet, WarehouseViewSet, WarehouseCategoryViewSet, ComboViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'productca_category', ProductCategoryViewSet)
router.register(r'warehouse', WarehouseViewSet)
router.register(r'warehousedetail', WarehouseCategoryViewSet)
router.register(r'combo', ComboViewSet)

urlpatterns = [

]
urlpatterns += router.urls
