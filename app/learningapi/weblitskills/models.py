from django.db import models
from learningapi.competencies.models import Competency
from learningapi.skills.models import Skill


class WebLitSkill(models.Model):
    """
    List of each web literacy skills with competencies
    """
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=100)
    competencies = models.ManyToManyField(
        Competency,
        blank=True,
        related_name='weblit_skills',
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name='weblit_skills',
    )

    def __str__(self):
        return str(self.name)
