from django.urls import re_path
from rest_framework.routers import DefaultRouter

from accounts.views import EmployeeViewSet,SupplierViewSet,CustomerViewSet
from accounts.views.user_list_viewset import UserListViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'user_list', UserListViewSet)


urlpatterns = [

]
urlpatterns += router.urls
