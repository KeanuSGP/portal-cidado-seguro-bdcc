from django.contrib import admin

from zeladoria.models import Categoria, Solicitacao

# Register your models here.
admin.site.register(Solicitacao)
admin.site.register(Categoria)