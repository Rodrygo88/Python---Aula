print("====== DESAFIO 091 ======") 

import random
import time

jogadores = {"jogador1": random.randint(1, 6), "jogador2": random.randint(1, 6), "jogador3": random.randint(1, 6), "jogador4": random.randint(1, 6),}


for k, v in jogadores.items():
    print(f"O {k} tirou {v}")
    time.sleep(0.5)


print("=== EM ORDEM ===")

ordenado = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

for k, v in ordenado.items():
    print(f"O {k} tirou {v}")
    time.sleep(0.5)

