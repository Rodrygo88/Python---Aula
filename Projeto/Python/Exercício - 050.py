print("====== DESAFIO 050 ======")

soma = 0

for c in range(0, 6):
    num = int(input(f" {c+1}º Número: "))
    teste =  num%2

    if teste == 0:
        soma += num

print(f"A soma de todos os números pares é {soma}!")