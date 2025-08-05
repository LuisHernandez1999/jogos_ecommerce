from rest_framework import serializers
from .models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    vendedor = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nome'  
    )

    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Jogo
        fields = ['id', 'nome', 'publicadora', 'preco', 'data_lancamento', 'vendedor']
