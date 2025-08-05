from django.db import models

class MeioRecebimento(models.Model):
    TIPOS = (
        ('PIX', 'PIX'),
        ('Cartao_de_Credito', 'Cartão de Crédito'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)

    
    chave_pix = models.CharField(max_length=100, blank=True, null=True)

    
    banco = models.CharField(max_length=50, blank=True, null=True)
    agencia = models.CharField(max_length=20, blank=True, null=True)
    conta = models.CharField(max_length=20, blank=True, null=True)
    tipo_conta = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.tipo
