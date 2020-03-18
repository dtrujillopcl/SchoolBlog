from django.db import models
from django.utils import timezone
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    texto = RichTextField(config_name='awesome_ckeditor')
    created_date = models.DateField(default=date.today)
    fecha_publicacion = models.DateField(blank=True, null=True)

    def publicacion(self):
        self.fecha_publicacion = date.today()
        self.save()

    def __str__(self):
        return self.titulo