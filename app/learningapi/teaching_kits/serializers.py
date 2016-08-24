from rest_framework import serializers

from learningapi.teaching_kits.models import TeachingKit
from learningapi.activities.models import (
    Activity,
)


class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializes links included in a project by only showing their
    URLS and placeholders
    """
    class Meta:
        model = Activity
        fields = (
            'title', 'subtitle', 'image_url', 'image_retina_url',
            'url', 'difficulty', 'duration', 'tags', 'skills',
            'authors', 'locale',
        )


class TeachingKitSerializer(serializers.ModelSerializer):
    """
    Serializes a teaching kit
    """
    activities = ActivitySerializer(many=True)

    class Meta:
        model = TeachingKit
