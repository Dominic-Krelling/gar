from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome.upper()

class Acessório(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição
    
class Cor(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__ (self):
        return self.descrição
    
class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10,decimal_places=2,default=0, null=True, blank= True)
    modelo = models.CharField(max_length=50)
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria,on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(
        Cor,on_delete=models.PROTECT, related_name="veiculos")


    def __str__ (self):
        return f"{self.modelo} ({self.id})"