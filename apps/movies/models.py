from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Programador(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    sobrenome = models.CharField(max_length=80, null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    linguagem = models.CharField(max_length=80, null=False, blank=False)
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'programadores'
        
    def __str__(self) -> str:
        return self.nome