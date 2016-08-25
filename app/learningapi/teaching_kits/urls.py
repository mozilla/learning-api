from django.conf.urls import url

from learningapi.teaching_kits.views import (
    TeachingKitListView,
    TeachingKitView,
)


urlpatterns = [
    # `/teachingkits` Gets a list of all Teaching Kits
    url('^$', TeachingKitListView.as_view(), name='teachkingkit-list'),
    # `/teachingkits/:pk` Gets a single Teaching Kit by its primary key,
    # where the named id is called pk by default in Django,
    # (see
    # https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/#performing-extra-work)
    url(r'^(?P<pk>[0-9]+)', TeachingKitView.as_view(), name='teachingkit'),
]
