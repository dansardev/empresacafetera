from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(verbose_name="URL amigable", max_length=150, unique=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    visible = models.BooleanField(verbose_name="¿Visible?", default=True)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title