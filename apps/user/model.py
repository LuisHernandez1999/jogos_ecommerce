from django.db import models

class users_cliente(models.Model):
    name = models.CharField(max_length=127)
    email = models.CharField(max_length=127)
    senha = models.CharField(max_length=9)
    celular = models.CharField(max_length=127)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
            models.Index(fields=["celular"]),
            models.Index(fields=["senha"]),
        ]
