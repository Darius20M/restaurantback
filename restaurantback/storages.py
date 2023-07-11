import os

from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class BaseStorage(S3Boto3Storage):
    def path(self, name):
        filename = os.path.join(settings.MEDIA_LOCAL_ROOT, name)
        print(filename)
        if not os.path.isfile(filename):
            try:
                with self.open(name, 'rb') as fileData:
                    contentFile = ContentFile(fileData.read())
                    fileData.close()
                fs = FileSystemStorage()
                fs.save(name, contentFile)
            except OSError:
                pass
        return filename


class StaticStorage(BaseStorage):
    location = '{0}/{1}'.format(settings.APP_NAME.lower(), 'static')
    default_acl = 'public-read'


class PublicMediaStorage(BaseStorage):
    location = '{0}/{1}'.format(settings.APP_NAME.lower(), 'media')
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(BaseStorage):
    location = '{0}/{1}'.format(settings.APP_NAME.lower(), 'private')
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False