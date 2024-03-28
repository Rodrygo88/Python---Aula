print("====== DESAFIO 052 ======")

num = int(input("Digite um número inteiro: "))
conta = 0

for c in range(1, num+1):
    teste = num%c
    if teste == 0:
        conta += 1

if conta == 2:
    print(f"O número {num} é um número PRIMO!")
else:
    print(f"O número {num} NÃO é um número PRIMO.")
