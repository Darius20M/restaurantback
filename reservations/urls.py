from django.urls import re_path
from rest_framework.routers import DefaultRouter

from reservations.views import ReservationViewSet, TableViewSet, CreateReservationViewSet, CancelReservationViewSet

router = DefaultRouter()
router.register(r'reservation', ReservationViewSet)
router.register(r'table', TableViewSet)

urlpatterns = [
    re_path(r'^create_reservation/', CreateReservationViewSet.as_view(), name='CreateReservation'),
    re_path(r'^cancel_reservation/', CancelReservationViewSet.as_view(), name='CancelReservation'),
]
urlpatterns += router.urls
