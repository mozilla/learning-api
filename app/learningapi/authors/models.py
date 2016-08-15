from django.db import models


class Author(models.Model):
    """
    The author that created an activity or teaching kit
    """
    name = models.CharField(max_length=300)
    url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
        help_text='URL to twitter or blog.',
    )

    def __str__(self):
        return str(self.name)
