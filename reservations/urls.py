from django.urls import re_path
from rest_framework.routers import DefaultRouter

from reservations.views import ReservationViewSet, TableViewSet, CreateReservationViewSet, CancelReservationViewSet, \
    confirm_reservation_view

router = DefaultRouter()
router.register(r'reservation', ReservationViewSet)
router.register(r'table', TableViewSet)

urlpatterns = [
    re_path(r'^create_reservation/', CreateReservationViewSet.as_view(), name='CreateReservation'),
    re_path(r'^cancel_reservation/', CancelReservationViewSet.as_view(), name='CancelReservation'),
    re_path(r'^reservations/confirm/(?P<reservation_id_b64>[A-Za-z0-9_\-]+)/(?P<token>[A-Za-z0-9_\-]+)/$',
            confirm_reservation_view, name='confirm_reservation'),

]
urlpatterns += router.urls
