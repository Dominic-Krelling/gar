from django.contrib import admin

from gar.models import Categoria, Marca, Acessório, Cor, Veiculo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(Acessório)
admin.site.register(Veiculo)