### Módulo MOEDAS ###

## Mais... ex107 ###

### Mais... ex108 ###

### Mais... ex109 ###

### Mais... ex110 ###

### Mais... ex111 ###

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



def resumo(valor, aum, dim):
    print("==="*10)
    print("RESUMO DO VALOR".center(30))
    print("==="*10)

    print(f"A metade: {metade(valor, True):^20}")

    print(f"O dobro: {dobro(valor, True):^20}")

    print(f"{aum}% de aumento: {aumentar(valor, aum, True):^20}")

    print(f"{dim}% de redução: {diminuir(valor, dim, True):^20}")

    print("==="*10)
