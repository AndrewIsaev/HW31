from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from ads.models import Advertisement, Category
from users.models import User


class AdSerializer(ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field="name")
    locations = SerializerMethodField()

    def get_locations(self, ad):
        return [location.name for location in ad.author.locations.all()]

    class Meta:
        model = Advertisement
        fields = "__all__"
