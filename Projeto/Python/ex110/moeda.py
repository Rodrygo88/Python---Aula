### Módulo MOEDAS ###

## Mais... ex107 ###

### Mais... ex108 ###

### Mais... ex109 ###

### Mais... ex110 ###

def metade(valor, op=False):
    met = valor/2
    
    if op == True:
        return moeda(met)
    else:
        return met

def dobro(valor, op=False):
    dob = valor*2
    
    if op == True:
        return moeda(dob)
    else:
        return dob

def aumentar(valor, por, op=False):
    aum = valor+valor*(por/100)
    
    if op == True:
        return moeda(aum)
    else:
        return aum


def diminuir(valor, por, op=False):
    dim = valor-valor*(por/100)
    
    if op == True:
        return moeda(dim)
    else:
        return dim




def moeda(valor):
    formatado = f"R${valor:.2f}"
    formatado = formatado.replace(".",",")
    return formatado

def resumo(valor):

