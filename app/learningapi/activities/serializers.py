from rest_framework import serializers

from learningapi.activities.models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    """
    Serializes an activity with embeded information including
    list of tags associated with that activity
    as simple strings.
    """
    tags = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)
    teaching_kits = serializers.StringRelatedField(many=True)
    authors = serializers.StringRelatedField(many=True)
    weblit_skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Activity
        fields = (
            'title', 'subtitle', 'image_url', 'image_retina_url',
            'url', 'difficulty', 'duration', 'tags', 'skills',
            'teaching_kits', 'authors', 'weblit_skills', 'locale',
        )
