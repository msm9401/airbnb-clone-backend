from django.db import models
from common.models import CommonModel
from django.core.validators import MaxValueValidator


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
    )
    review = models.TextField(
        default="",
    )
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"{self.user} : {self.rating}⭐"
