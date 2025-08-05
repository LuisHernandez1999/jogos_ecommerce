import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.produto.services.services import cadastrar_jogo
from apps.vendedor.models import user_vendedor

@csrf_exempt
def cadastrar_jogo_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nome = data.get('nome')
            publicadora = data.get('publicadora')
            preco = data.get('preco')
            data_lancamento = data.get('data_lancamento')
            vendedor_name= data.get('vendedor_name')

            # ✅ Buscar pelo modelo correto: user_vendedor
            vendedor = user_vendedor.objects.get(name=vendedor_name)

            jogo = cadastrar_jogo(nome, publicadora, preco, data_lancamento, vendedor)

            return JsonResponse({
                "message": "Jogo criado com sucesso",
                "jogo_id": jogo.id
            }, status=201)

        except user_vendedor.DoesNotExist:
            return JsonResponse({"error": "Vendedor não encontrado."}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método não permitido."}, status=405)
