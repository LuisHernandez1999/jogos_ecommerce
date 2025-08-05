from django.db import models
from apps.user.model import users_cliente  
from apps.meio_recebimento.models import MeioRecebimento

class user_vendedor(users_cliente):
    cnpj = models.CharField(max_length=18, unique=True)
    meio_recebimento = models.ForeignKey(MeioRecebimento, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["cnpj"]),
            models.Index(fields=["meio_recebimento"]),
        ]
