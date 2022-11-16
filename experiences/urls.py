from django.urls import path
from .views import Perks, PerksDetail


urlpatterns = [
    path("", Perks.as_view()),
    path("<int:pk>", PerksDetail.as_view()),
]
