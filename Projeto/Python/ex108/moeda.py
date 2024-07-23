### Módulo MOEDAS ###

## Mais... ex107 ###

## Mais... ex108 ###

def metade(valor):
    met = valor/2
    return met

def dobro(valor):
    dob = valor*2
    return dob

def aumentar(valor, por):
    aum = valor+valor*(por/100)
    return aum

def diminuir(valor, por):
    red = valor-valor*(por/100)
    return red


def moeda(valor):
    formatado = f"R${valor:.2f}"
    formatado = formatado.replace(".",",")
    return formatado
    