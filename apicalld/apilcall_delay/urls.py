# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from apicalld import urls as apilcall_delay_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('apicalls/', include(apilcall_delay_urls)),
]