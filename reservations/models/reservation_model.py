from django.db import models
from django.utils import timezone
from reservations.utils.constants import STATUS_R
from django.conf import settings


class ReservationModel(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reserve', on_delete=models.PROTECT)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    table = models.ForeignKey('reservations.TableModel', on_delete=models.CASCADE)
    checkin = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_R, default=STATUS_R.pending, null=False,
                              blank=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_reservation_t'
        app_label = 'reservations'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ReservationModel, self).save(*args, **kwargs)
