from rest_framework import serializers
from .models import MeioRecebimento

class MeioRecebimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeioRecebimento
        fields = '__all__'
    
    def validate(self, data):
        tipo = data.get('tipo')
        chave_pix = data.get('chave_pix')
        banco = data.get('banco')
        agencia = data.get('agencia')
        conta = data.get('conta')

        if tipo == 'PIX':
            if not chave_pix:
                raise serializers.ValidationError("chave PIX deve ser informada quando o tipo for PIX.")
        else:
           
            if chave_pix:
                raise serializers.ValidationError("chave PIX deve estar vazia para tipos diferentes de PIX.")

        
        if banco and len(banco) > 50:
            raise serializers.ValidationError("o nome do banco nao pode exceder 50 caracteres.")

        if agencia and len(agencia) > 20:
            raise serializers.ValidationError("a agencia nao pode exceder 20 caracteres.")

        if conta and len(conta) > 20:
            raise serializers.ValidationError("a conta nao pode exceder 20 caracteres.")
        
        return data
