from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdimin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "created_at",
        "updated_at",
    )

    lsit_filter = ("kind",)
