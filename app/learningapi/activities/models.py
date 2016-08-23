from django.db import models
from learningapi.teaching_kits.models import TeachingKit
from learningapi.authors.models import Author
from learningapi.skills.models import Skill
from learningapi.weblitskills.models import WebLitSkill


class Tag(models.Model):
    """
    Tags used to describe properties of an activity (such as what
    programming languages does the activity teaches, etc.) and to
    enable filtering activities by these properties
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.name)


class Activity(models.Model):
    """
    An activity to teach people about different subject on the web
    """
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text='URL to a regular quality image.',
    )
    image_retina_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text='URL to a retina quality image.',
    )
    url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text='URL to an activity.',
    )
    difficulty = models.CharField(
        max_length=50,
        default='Beginner',
        choices=(
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Beginner mobile users', 'Beginner mobile users'),
            ('13+', '13+'),
            ('JavaScript beginners', 'JavaScript beginners'),
        ),
        help_text='Difficulty levels for an activity'
    )
    duration = models.CharField(
        max_length=100,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='activities',
        blank=True,
    )
    skills = models.ManyToManyField(
        Skill,
        related_name='activities',
        blank=True,
    )
    teaching_kits = models.ManyToManyField(
        TeachingKit,
        through='TeachingKitActivity',
        related_name='activities',
        blank=True,
    )
    authors = models.ManyToManyField(
        Author,
        related_name='activities',
        blank=True,
    )
    weblit_skills = models.ManyToManyField(
        WebLitSkill,
        related_name='activities',
        blank=True,
    )
    locale = models.CharField(
        max_length=20,
        default='en-US',
        blank=True,
    )

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "activities"


class TeachingKitActivity(models.Model):
    """
    An Activity is part of a Teaching Kit and stored them in order
    """
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    teaching_kit = models.ForeignKey(TeachingKit, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(
        default=0,
    )
