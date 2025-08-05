from django.db import models
from apps.vendedor.models import user_vendedor

class Jogo(models.Model):  
    nome = models.CharField(max_length=127)
    publicadora = models.CharField(max_length=127)
    preco = models.CharField(max_length=7)  
    data_lancamento = models.DateField()   
    vendedor = models.ForeignKey(user_vendedor, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=["nome"]),
            models.Index(fields=["publicadora"]),
            models.Index(fields=["data_lancamento"]), 
        ]
