print("====== DESAFIO 028 ======")
import random
import time

print("Jogo de adivinha!!! ")
num = int(input("Qual número estou pensando entre 0 e 5 ? "))
escolha = random.randint(0,5)
print("Processando...")
time.sleep(3)
if num == escolha:
    print("Você acertou, parabéns!!! \nPensei no {}.".format(escolha))
else:
    print("Errou! Pensei no {}.".format(escolha))

print("Fim.")