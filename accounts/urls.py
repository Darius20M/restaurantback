from django.urls import re_path
from rest_framework.routers import DefaultRouter

from accounts.views import EmployeeViewSet,SupplierViewSet,CustomerViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'customer', CustomerViewSet)

urlpatterns = [

]
urlpatterns += router.urls
