from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from apps.meio_recebimento.service.service import criar_meio_recebimento

@csrf_exempt
def criar_meio_recebimento_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'metodo nao permitido'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON invalido'}, status=400)

    tipo = data.get('tipo')
    chave_pix = data.get('chave_pix')
    banco = data.get('banco')
    agencia = data.get('agencia')
    conta = data.get('conta')
    tipo_conta = data.get('tipo_conta')

    try:
        meio = criar_meio_recebimento(
            tipo=tipo,
            chave_pix=chave_pix,
            banco=banco,
            agencia=agencia,
            conta=conta,
            tipo_conta=tipo_conta
        )
    except ValidationError as e:
        return JsonResponse({'error': e.message_dict if hasattr(e, 'message_dict') else e.messages}, status=400)

    return JsonResponse({
        'message': 'meio de pagamento criado com sucesso',
        'id': meio.id,
    }, status=201)
