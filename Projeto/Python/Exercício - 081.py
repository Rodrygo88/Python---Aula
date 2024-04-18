print("====== DESAFIO 081 ======")  

lista = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    op = str(input("Quer adicionar outro? S/N ")).strip().upper()[0]
    if op == "N":
        break


print(f"Foram digitados {len(lista)} números!")

print(sorted(lista, reverse=True))

if 5 in lista:
    print("O número 5, está SIM na lista!")
else:
    print("O número 5, NÃO na lista!")
