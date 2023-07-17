from django.urls import re_path
from rest_framework.routers import DefaultRouter

from security.views import GoogleLoginView
from allauth.socialaccount.views import signup


router = DefaultRouter()

urlpatterns = [
    re_path('auth/google/login/', GoogleLoginView.as_view(), name='google_login'),

]
urlpatterns += router.urls
