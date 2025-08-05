import json
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from apps.criar_conta.service.criar_conta_sevice import criar_cliente, criar_vendedor
from apps.meio_recebimento.models import MeioRecebimento

@csrf_protect
@require_http_methods(["POST"])
def criar_conta_view(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON invalido"}, status=400)

    tipo = data.get('tipo')  
    name = data.get('name')
    email = data.get('email')
    senha = data.get('senha')
    celular = data.get('celular')

    if not all([tipo, name, email, senha, celular]):
        return JsonResponse({"error": "campos obrigatorios faltando."}, status=400)

    if tipo == 'cliente':
        usuario = criar_cliente(name, email, senha, celular)

    elif tipo == 'vendedor':
        cnpj = data.get('cnpj')
        meio_recebimento_id = data.get('meio_recebimento_id')

        if not cnpj:
            return JsonResponse({"error": "CNPJ e obrigatorio para vendedor."}, status=400)

        meio_recebimento = None
        if meio_recebimento_id:
            try:
                meio_recebimento = MeioRecebimento.objects.get(id=meio_recebimento_id)
            except MeioRecebimento.DoesNotExist:
                return JsonResponse({"error": "meio de recebimento invalido."}, status=400)
        usuario = criar_vendedor(name, email, senha, celular, cnpj, meio_recebimento)
    else:
        return JsonResponse({"error": "tipo de usuario invalido."}, status=400)

    return JsonResponse({
        "id": usuario.id,
        "name": usuario.name,
        "email": usuario.email,
        "celular": usuario.celular,
    }, status=201)
