from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from learningapi.activities.models import Activity
from learningapi.activities.serializers import (
    ActivitySerializer,
)


class ActivityListView(ListAPIView):
    """
    A view that allow listing all the activities
    in the database
    """
    queryset = Activity.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ActivitySerializer


class ActivityView(RetrieveAPIView):
    """
    A view that allow listing of a single activity
    by providing their `id` as a parameter
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    pagination_class = None
