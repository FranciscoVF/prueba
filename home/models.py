from django.db import models

# Create your models here.

class ModelExample(models.Model):
    animal = models.CharField(max_length=64)
    ejemplares = models.IntegerField()

    def __str__(self):
        return self.animal
