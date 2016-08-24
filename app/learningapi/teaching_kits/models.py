from django.db import models
from learningapi.authors.models import Author


class TeachingKit(models.Model):
    """
    Set of activities that used as kit to teach people about certain topics
    """
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField(
        blank=True,
        null=True,
    )
    authors = models.ManyToManyField(
        Author,
        related_name='teaching_kits',
        blank=True,
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

    def __str__(self):
        return str(self.title)
