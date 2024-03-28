print("====== DESAFIO 055 ======")

maior = 0
menor = 0

for c in range(0, 5):
    peso = float(input(f"Peso da {c+1}º pessoa: "))

    if c == 0:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print(f"O maior peso foi de {maior}kg!")
print(f"O menor peso foi de {menor}kg!")