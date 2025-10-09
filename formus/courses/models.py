from django.db import models

class Course(models.Model):
    code = models.CharField("Codigo", max_length=50)
    title = models.CharField("Título", max_length=120)
    description = models.TextField("Descripción")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]