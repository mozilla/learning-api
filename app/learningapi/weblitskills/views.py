from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from learningapi.weblitskills.models import WebLitSkill
from learningapi.weblitskills.serializers import (
    WebLitSkillSerializer,
)


class WebLitSkillListView(ListAPIView):
    """
    A view that allow listing all the weblit skills
    in the database
    """
    queryset = WebLitSkill.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = WebLitSkillSerializer


class WebLitSkillView(RetrieveAPIView):
    """
    A view that allow listing of a single weblit skill
    by providing their `id` as a parameter
    """
    queryset = WebLitSkill.objects.all()
    serializer_class = WebLitSkillSerializer
    pagination_class = None
