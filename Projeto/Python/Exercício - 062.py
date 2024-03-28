print("====== DESAFIO 062 ======")

print("10 termos de uma PA!")
termo = int(input("Primerio termo: "))
razão = int(input("Razão: "))

cont = 10
c = 0

while cont != 0:
    print(f"{termo+c*razão}", end=" -> ")
    cont -= 1
    c += 1

    if cont == 0:
        print(" ")
        mais = int(input("Que ver mais quantos termos dessa PA? (Digite 0 para sair!) "))
        cont += mais

print("ACABOU")