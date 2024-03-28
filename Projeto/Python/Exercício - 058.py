print("====== DESAFIO 058 ======")

import random
import time

escolha = random.randint(0,10)
print("Jogo de adivinha!!! ")

num = -1
cont = 0

while num != escolha:
    num = int(input("Qual número estou pensando entre 0 e 10? "))
    print("Processando...")
    time.sleep(1)
    if num != escolha:
        print("Errou! Tente novamente!!.")
        if num < escolha:
            print("Pensei em um maior...")
        elif num > escolha:
            print("Pensei em um menor...")
        cont += 1
    else:
        num = escolha

print("Você acertou, parabéns!!! \nPensei no número {}.".format(escolha))
print(f"Você acertou com {cont+1} tentativas!.")