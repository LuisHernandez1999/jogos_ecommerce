from django.core.exceptions import ValidationError
from django.db import transaction
from apps.meio_recebimento.models import MeioRecebimento

@transaction.atomic
def criar_meio_recebimento(
        tipo: str,
        chave_pix: str = None,
        banco: str = None,
        agencia: str = None,
        conta: str = None,
        tipo_conta: str = None
    ) -> MeioRecebimento:

        tipos_validos = [choice[0] for choice in MeioRecebimento.TIPOS]
        if tipo not in tipos_validos:
            raise ValidationError(f"tipo invalido. Escolha entre {tipos_validos}")

        if tipo == 'PIX' and (not chave_pix or chave_pix.strip() == ''):
            raise ValidationError("chave PIX e obrigatoria para tipo 'PIX'.")

        if tipo == 'Cartao_de_Credito' and (not banco or banco.strip() == ''):
            raise ValidationError("banco e obrigatorio para tipo 'Cartao_de_Credito'.")

        meio = MeioRecebimento(
            tipo=tipo,
            chave_pix=chave_pix if tipo == 'PIX' else None,
            banco=banco if tipo == 'Cartao_de_Credito' else None,
            agencia=agencia,
            conta=conta,
            tipo_conta=tipo_conta,
        )
        meio.full_clean() 
        meio.save()
        return meio
