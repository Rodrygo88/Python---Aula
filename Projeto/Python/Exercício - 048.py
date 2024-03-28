print("====== DESAFIO 048 ======")

soma= 0 

for c in range(1, 501, 2):
    teste =  c%3
    if teste == 0:
        soma += c

print(f"A soma dos números ímpares e multiplos de 3 da um total de {soma}! ")