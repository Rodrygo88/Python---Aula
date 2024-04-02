print("====== DESAFIO 074 ======")  

import random

tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

print("Valores sorteados: ", end="")
for num in tupla:
    print(num, end=" ")    

print("\n")

print(f"O MAIOR número da tupla é {max(tupla)}")
print(f"O MENOR número da tupla é {min(tupla)}")