from django.db import models

from gar.models import Acessorio, Cor, Modelo, Categoria, Marca
from uploader.models import Image

class Veiculo(models.Model):
    descrição = models.CharField(max_length=99)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10,decimal_places=2,default=0, null=True, blank= True)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(
        Cor,on_delete=models.PROTECT, related_name="veiculos")
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    foto = models.ManyToManyField(Image, related_name="Veiculo")


    def __str__ (self):
        return f"{self.ano} | {self.cor} | {self.modelo}"

    class Meta:
        verbose_name = "Veiculo"