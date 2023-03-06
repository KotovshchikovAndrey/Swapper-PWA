from django.contrib import admin
from django.urls import include, path

from app import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/profile/", include("profile_app.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
