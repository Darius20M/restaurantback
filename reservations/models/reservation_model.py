from django.db import models
from django.utils import timezone
from reservations.utils.constants import STATUS_R
from django.conf import settings


class ReservationModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reserve', on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    table = models.ForeignKey('reservations.TableModel', on_delete=models.CASCADE)
    checkin = models.DateField(default=timezone.now)
    hour = models.CharField()
    status = models.CharField(max_length=20, choices=STATUS_R, default=STATUS_R.pending, null=False,
                              blank=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_reservation_t'
        app_label = 'reservations'
        verbose_name = ('Reservacion')
        verbose_name_plural = ('Reservaciones')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ReservationModel, self).save(*args, **kwargs)
