print("====== DESAFIO 100 ======") 

import random
import time

def sorteio(lista):
    print("SORTEANDO 5 VALORES para lista: ")

    for c in range(0, 5):
        valor = random.randint(1, 10)
        lista.append(valor)
        print(valor, end=" ")
        time.sleep(0.5)
    print("Pronto!")


def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f"Somando os valores pares da lista {lista}:")
    print(f"O total dos pares é {soma}")

numeros = []

sorteio(numeros)

somaPar(numeros)

