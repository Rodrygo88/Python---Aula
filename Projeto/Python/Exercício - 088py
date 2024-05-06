print("====== DESAFIO 088 ======") 

import random
import time

jogos = []
jogo = []

quantos = int(input("Quantos jogos você quer que eu sorteie? "))

for c in range(0, quantos):
    jogo.clear()
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)

    jogos.append(jogo[:])
    

print(f"Sorteando {quantos} JOGOS!!!")
for i, c in enumerate(jogos):
    print(f"Jogo {i+1}: {c}")
    time.sleep(1)

print("FIM")