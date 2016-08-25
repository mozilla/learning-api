from rest_framework import serializers

from learningapi.weblitskills.models import WebLitSkill


class WebLitSkillSerializer(serializers.ModelSerializer):
    """
    Serializes a weblit skill
    """
    activities = serializers.StringRelatedField(many=True)

    class Meta:
        model = WebLitSkill
