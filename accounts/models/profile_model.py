from django.conf import settings
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from restaurantback.storages import PrivateMediaStorage


def path_profile_avatar(self, filename):
    return "accounts/%s/%s" % (self.user.username, filename)


class ProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to=path_profile_avatar, storage=PrivateMediaStorage(), default=None, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'acc_profile'
        app_label = 'accounts'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ProfileModel, self).save(*args, **kwargs)