from rest_framework import serializers

from learningapi.weblitskills.models import WebLitSkill


class WebLitSkillSerializer(serializers.ModelSerializer):
    """
    Serializes a weblit skill
    """
    class Meta:
        model = WebLitSkill
