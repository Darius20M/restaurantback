"""
URL configuration for restaurantback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns



urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('reservations/', include('reservations.urls')),
    re_path('orders/', include('orders.urls')),
    re_path('accounts/', include('accounts.urls')),
    re_path('products/', include('products.urls')),
    re_path('billings/', include('billings.urls')),
    re_path('security/', include('security.urls')),
    re_path('docs/', include_docs_urls(title='Restaurant API')),
    re_path('auth/', include('dj_rest_auth.urls')),
    re_path('auth/registration/', include('dj_rest_auth.registration.urls')),

]
