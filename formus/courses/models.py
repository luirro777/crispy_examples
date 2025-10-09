# courses/models.py
from django.db import models

class Course(models.Model):
    title = models.CharField("Título", max_length=120)
    code  = models.CharField("Código", max_length=20, unique=True)
    description = models.TextField("Descripción")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]