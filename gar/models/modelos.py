from django.db import models
from .marcas import Marca


class Modelo(models.Model):
    descricao = models.CharField(max_length=70)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelo")

    def __str__(self):
        return f"{self.descricao} | {self.marca}"

class Meta:
    verbose_name_plural = "Modelos"