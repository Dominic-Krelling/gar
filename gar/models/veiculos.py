from django.db import models
from .acessorios import Acessorio
from .categorias import Categoria
from .cores import Cor
from .marcas import Marca
from .modelos import Modelo
from uploader.models import Image

class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10,decimal_places=2,default=0, null=True, blank= True)
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos")
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria,on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(
        Cor,on_delete=models.PROTECT, related_name="veiculos")
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    foto = models.ForeignKey( Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None )


    def __str__ (self):
        return f"{self.marca} | {self.ano} | {self.cor} | {self.modelo}"