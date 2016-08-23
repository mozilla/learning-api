from django.db import models


class Competency(models.Model):
    """
    Competency text for Weblit skills or skills page
    """
    text = models.TextField()

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = "competencies"
