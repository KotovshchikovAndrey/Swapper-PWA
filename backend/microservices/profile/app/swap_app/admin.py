from django.contrib import admin
from swap_app.models import Swap, SwapHistory


@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    pass


@admin.register(SwapHistory)
class SwapHistoryAdmin(admin.ModelAdmin):
    pass
