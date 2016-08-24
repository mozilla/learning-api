from django.conf.urls import url

from learningapi.activities.views import (
    ActivityListView,
    ActivityView,
)


urlpatterns = [
    # `/activities` Gets a list of all activities
    url('^$', ActivityListView.as_view(), name='activity-list'),
    # `/activities/:pk` Gets a single activity by its primary key,
    # where the named id is called pk by default in Django,
    # (see
    # https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/#performing-extra-work)
    url(r'^(?P<pk>[0-9]+)', ActivityView.as_view(), name='activity'),
]
