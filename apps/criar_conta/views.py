import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from apps.criar_conta.service.criar_conta_sevice import criar_cliente, criar_vendedor
from apps.meio_recebimento.models import MeioRecebimento
from apps.user.model import users_cliente
from apps.vendedor.models import user_vendedor

@csrf_exempt
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

   
    celular_ja_existe = (
        users_cliente.objects.filter(celular=celular).exists() or
        user_vendedor.objects.filter(celular=celular).exists()
    )
    if celular_ja_existe:
        return JsonResponse({"error": "ja existe uma conta com este número de celular."}, status=400)

   
    if tipo == 'cliente':
        usuario = criar_cliente(name, email, senha, celular)

    
    elif tipo == 'vendedor':
        cnpj = data.get('cnpj')
        meio_recebimento_id = data.get('meio_recebimento_id')

        if not cnpj:
            return JsonResponse({"error": "CNPJ e obrigatório para vendedor."}, status=400)

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
        "mensagem": f"conta criada com sucesso para {usuario.name}!",
        "name": usuario.name
    }, status=201)
