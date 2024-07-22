print("====== DESAFIO 101 ======") 
def voto(nascimento):
    import datetime

    atual = datetime.datetime.now()
    data = atual.date()
    atual = data.year

    idade = atual - nascimento

    if idade < 16:
        return f"Com {idade} anos: NEGADO"
    elif idade >= 65:
        return f"Com {idade} anos: OPCIONAL"
    else:
        return f"Com {idade} anos: OBRIGATÓRIO"

ano = int(input("Ano de nascimento: "))
print(voto(ano))