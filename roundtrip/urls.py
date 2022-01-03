from django.contrib import admin
from django.urls import path

from roundtrip.views import weather_sync, weather_async

urlpatterns = [
    path("sync/", weather_sync),
    path("async/", weather_async),
    path('admin/', admin.site.urls),
]
