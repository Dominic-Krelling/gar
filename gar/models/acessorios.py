from django.db import models


class Acessorio(models.Model):
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição

    class Meta:
        verbose_name_plural="Acessórios"