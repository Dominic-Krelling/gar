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
    
class Modelo(models.Model):
    descricao = models.CharField(max_length=70)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelo")

    def __str__(self):
        return f"{self.descricao} | {self.marca}"

class Acessorio(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição

    class Meta:
        verbose_name_plural="Acessórios"
    
class Cor(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__ (self):
        return self.descrição
    
    class Meta:
        verbose_name_plural = "Cores"
    
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


    def __str__ (self):
        return f"{self.marca} | {self.ano} | {self.cor} | {self.modelo}"