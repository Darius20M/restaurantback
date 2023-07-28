from django.urls import re_path
from rest_framework.routers import DefaultRouter

from accounts.views import EmployeeViewSet,SupplierViewSet,CustomerViewSet
from accounts.views.detele_user_viewset import DeleteAccountViewSet
from accounts.views.user_list_viewset import UserListViewSet

router = DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'user_list', UserListViewSet)


urlpatterns = [
    re_path(r'^delete_user/', DeleteAccountViewSet.as_view(), name='DeleteAccountViewSet'),

]
urlpatterns += router.urls
