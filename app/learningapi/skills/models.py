from django.db import models


class Skill(models.Model):
    """
    Skill object that used to describe list of activities
    """
    name = models.CharField(max_length=150)
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

    def __str__(self):
        return str(self.name)
