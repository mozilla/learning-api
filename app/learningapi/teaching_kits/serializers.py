from rest_framework import serializers

from learningapi.teaching_kits.models import TeachingKit


class TeachingKitSerializer(serializers.ModelSerializer):
    """
    Serializes a teaching kit
    """
    activities = serializers.StringRelatedField(many=True)

    class Meta:
        model = TeachingKit
