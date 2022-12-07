from rest_framework import serializers
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from .models import Amenity, Room


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = [
            "name",
            "description",
        ]


class RoomListSerializer(serializers.ModelSerializer):

    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Room
        fields = [
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
            "photos",
        ]

    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner


class RoomDetailSerializer(serializers.ModelSerializer):

    owner = TinyUserSerializer(
        read_only=True,
    )
    amenities = AmenitySerializer(
        many=True,
        read_only=True,
    )
    category = CategorySerializer(
        read_only=True,
    )

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner

    class Meta:
        model = Room
        fields = "__all__"
