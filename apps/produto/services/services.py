from ..models import Jogo

def cadastrar_jogo(nome, publicadora, preco, data_lancamento, vendedor):
    return Jogo.objects.create(
        nome=nome,
        publicadora=publicadora,
        preco=preco,
        data_lancamento=data_lancamento,
        vendedor=vendedor  # ✅ nome do campo correto
    )
