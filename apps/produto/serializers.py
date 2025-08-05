from rest_framework import serializers
from .models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    # serializa o vendedor mostrando apenas o nome 
    vendedor = serializers.SlugRelatedField(
        read_only=True,
        slug_field='nome'  # ajuste waqui, pra exibir apenas o nome do vendedor 
    )

    preco = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Jogo
        fields = ['id', 'nome', 'publicadora', 'preco', 'data_lancamento', 'vendedor']
