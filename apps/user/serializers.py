from rest_framework import serializers
from apps.user.model import users_cliente

class users_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_cliente
        fields = ['id', 'name', 'email', 'senha', 'celular']
