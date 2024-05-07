print("====== DESAFIO 087 ======") 
lista = []

cont1= 0
cont2= 0

pares = 0
coluna = 0
linha_maior = 0

for c in range(0, 9):
    valor = int(input(f"Valor para a posição [{cont1}, {cont2}]: "))
    lista.append(valor)

    cont2 +=1

    if c == 2 or c == 5:
        cont1+= 1
        cont2 -= 3
    
    if valor % 2 == 0:
        pares += valor


for i, c in enumerate(lista):
    print(f"[ {c:^5} ]", end="")

    if i == 3 or i == 4 or i == 5:
        if i == 3:
            linha_maior = c
        else:
            if c > linha_maior:
                linha_maior = c

    if i == 2 or i == 5 or i == 8:
        coluna += c
        print("") 

print(f"A soma dos valores pares é {pares}.")
print(f"A soma dos valores da terceira coluna é {coluna}.")
print(f"O maior valor da segunda linha é {linha_maior}.")
