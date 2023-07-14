from restaurantback.wsgi import *
from datetime import timedelta

from reservations.models import ReservationModel
from django.utils import timezone


def update_state():
    reservation: ReservationModel = ReservationModel.objects.filter(status__in=['Pending', 'Confirmed'])

    for data in reservation:
        now = timezone.now()
        checkin = data.checkin + timedelta(minutes=30)
        print(now)
        if now > checkin:
            data.status = 'No Show'
            data.table.status = "Available"
            data.table.save()
            data.save()
            print('hola')
