from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):

    """Wishlist Model Definition"""

    name = models.CharField(
        max_length=30,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room_wishlists = models.ManyToManyField(
        "rooms.Room",
    )
    experience_wishlists = models.ManyToManyField(
        "experiences.Experience",
    )

    def __str__(self) -> str:
        return self.name
