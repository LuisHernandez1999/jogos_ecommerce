from apps.user.model import users_cliente
from apps.vendedor.models import user_vendedor
from django.core.exceptions import ValidationError

def celular_existe(celular):
    
    clientes_qs = users_cliente.objects.filter(celular=celular).values_list('celular', flat=True)
    vendedores_qs = user_vendedor.objects.filter(celular=celular).values_list('celular', flat=True)


    celulares_unidos = clientes_qs.union(vendedores_qs)

    return celulares_unidos.exists()

def criar_cliente(name, email, senha, celular):
    if celular_existe(celular):
        raise ValidationError("ja existe um cliente ou vendedor com este número de celular.")
    
    return users_cliente.objects.create(
        name=name,
        email=email,
        senha=senha,
        celular=celular
    )

def criar_vendedor(name, email, senha, celular, cnpj, meio_recebimento):
    if celular_existe(celular):
        raise ValidationError("ja existe um cliente ou vendedor com este número de celular.")
    
    return user_vendedor.objects.create(
        name=name,
        email=email,
        senha=senha,
        celular=celular,
        cnpj=cnpj,
        meio_recebimento=meio_recebimento
    )
