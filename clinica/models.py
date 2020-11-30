from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ModeloBase(models.Model):
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    hora_actualizado = models.DateTimeField(auto_now_add=True)
    horario = models.DateTimeField(auto_now_add=True)
    usuario_actualizar = models.IntegerField(blank = True, null = True)

class Meta:
    abstract = True

class Category(ModeloBase):
    desc_servicio = models.CharField(
    max_length = 128,
    help_text = "Tipo de servicio",
    unique = False
    )
class Meta:
    verbose_name_plural = "Categories"

def __str__(self):
    return "{}".format(self.desc_category)


class SubCategory(ModeloBase):
    categoria = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.CharField(max_length=128, unique=True, help_text="SubCategory Description")


class Meta:
    verbose_name_plural = "SubCategories"

def __str__(self):
    return "{}".format(self.description)





    class Obras(BaseModel):
    typo =   models.ForeignKey(Category, on_delete = models.CASCADE)
    autor = models.ForeignKey(Autores, on_delete = models.CASCADE)
    precio = models.IntegerField(blank = True, null = True, default = 100)
    descripcion = models.CharField(max_length=128,
        unique=True,
        help_text="Breve descripcion de la obra")

def __str__(self):
    return "{}".format(self.descripcion)
