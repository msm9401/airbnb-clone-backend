from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "user",
        "room",
        "experience",
        "rating",
    )
