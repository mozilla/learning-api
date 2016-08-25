from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from learningapi.teaching_kits.models import TeachingKit
from learningapi.teaching_kits.serializers import (
    TeachingKitSerializer,
)


class TeachingKitListView(ListAPIView):
    """
    A view that allow listing all the teaching kits
    in the database
    """
    queryset = TeachingKit.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = TeachingKitSerializer


class TeachingKitView(RetrieveAPIView):
    """
    A view that allow listing of a single activity
    by providing their `id` as a parameter
    """
    queryset = TeachingKit.objects.all()
    serializer_class = TeachingKitSerializer
    pagination_class = None
