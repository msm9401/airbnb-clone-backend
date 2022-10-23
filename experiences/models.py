from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=50,
        default="서울",
    )
    name = models.CharField(
        max_length=50,
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=150,
    )
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """Included in Experience"""

    name = models.CharField(
        max_length=50,
    )
    details = models.CharField(
        max_length=150,
        blank=True,
    )
    explanation = models.TextField(
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
