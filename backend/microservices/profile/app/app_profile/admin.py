from django.contrib import admin
from app_profile import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Swap)
class SwapAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SwapHistory)
class SwapHistoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("swaps",)
