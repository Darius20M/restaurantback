import os
from reservations.tasks import update_state
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurantback.settings')
import django

django.setup()

if __name__ == '__main__':

    update_state()