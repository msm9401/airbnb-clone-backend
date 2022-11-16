from django.urls import path
from . import views

urlpatterns = [
    path("", views.Amenities.as_view()),
    path("<int:pk>", views.AmenityDetail.as_view()),
]
