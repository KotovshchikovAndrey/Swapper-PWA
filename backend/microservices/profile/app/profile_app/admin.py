from django.contrib import admin
from profile_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
