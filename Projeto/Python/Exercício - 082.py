print("====== DESAFIO 082 ======")  

lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    op = str(input("Quer adicionar outro? S/N ")).strip().upper()[0]
    if op == "N":
        break

lista_par = []
lista_impar = []

for item in lista:
    if item % 2 == 1:
        lista_impar.append(item)
    else:
        lista_par.append(item)
    

print(f"Lista padrão: {lista}")

print(f"Lista impar: {lista_impar}")

print(f"Lista par: {lista_par}")