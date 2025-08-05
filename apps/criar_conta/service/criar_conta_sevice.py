from apps.user.model import users_cliente
from  apps.vendedor.models import user_vendedor


def criar_cliente(name, email, senha, celular):
    return users_cliente.objects.create(
        name=name,
        email=email,
        senha=senha,
        celular=celular
    )

def criar_vendedor(name, email, senha, celular, cnpj, meio_recebimento):
    return user_vendedor.objects.create(
        name=name,
        email=email,
        senha=senha,
        celular=celular,
        cnpj=cnpj,
        meio_recebimento=meio_recebimento
    )
