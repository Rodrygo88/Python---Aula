print("====== DESAFIO 064 ======")

num = 0
soma = 0
cont = -1

while num != 999:
    num = int(input("Digite um número para somar: (999 para finalizar) "))
    cont += 1

    soma += num

print(f"Foram digitados {cont} números e a soma de todos eles é de {soma-999}!")
