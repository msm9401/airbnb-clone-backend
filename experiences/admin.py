from django.contrib import admin
from .models import Experience, Perk


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "country",
        "city",
        "host",
        "price",
        "start",
        "end",
    )

    list_filter = (
        "country",
        "city",
        "host",
        "price",
    )


@admin.register(Perk)
class PerkAdmin(admin.ModelAdmin):

    list_display = ("name", "details")
