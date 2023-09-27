from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from apps.movies.models import Programador
# Register your models here.

@admin.register(Programador)
class ProgramadorAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome', 'idade', 'linguagem')
    list_filter = ('linguagem',)
    readonly_fields = ('criado_por',)
    
    def save_model(self, request, obj, form, change): # ao salvar o programador ele adiciona o usuario logado
        usuario = request.user 
        obj.criado_por = usuario
        super(ProgramadorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request): # somente traz os programadores que o usuario logado cadastrou
        qs = super(ProgramadorAdmin, self).get_queryset(request)
        
        if not  request.user.is_superuser:
            qs = qs.filter(criado_por=request.user)
            return qs
        return qs
        