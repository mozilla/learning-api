from django.conf.urls import url

from learningapi.weblitskills.views import (
    WebLitSkillListView,
    WebLitSkillView,
)


urlpatterns = [
    # `/weblitskills` Gets a list of all Weblit skills
    url('^$', WebLitSkillListView.as_view(), name='weblitskill-list'),
    # `/weblitskills/:pk` Gets a single weblit skills by its primary key,
    # where the named id is called pk by default in Django,
    # (see
    # https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-display/#performing-extra-work)
    url(r'^(?P<pk>[0-9]+)', WebLitSkillView.as_view(), name='weblitskill'),
]
