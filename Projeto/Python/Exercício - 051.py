print("====== DESAFIO 051 ======")

print("10 termos de uma PA!")
termo = int(input("Primerio termo: "))
razão = int(input("Razão: "))

for c in range(0, 10):
    print(f"{termo+c*razão}", end=" -> ")

print("ACABOU")