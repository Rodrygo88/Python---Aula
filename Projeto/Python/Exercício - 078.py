print("====== DESAFIO 078 ======")  

lista = []

for c in range(0, 5):
    lista.append(int(input(f"NÚMERO DA POSIÇÃO {c} : ")))

print(lista)

print(f"O maior valor digitado foi o {max(lista)} na posição: ", end="")

for c in range(0, 5):
    if max(lista) == lista[c]:
        print(c, end="... ")


print(f"\nO menor valor digitado foi o {min(lista)} na posição: ", end="")

for c in range(0, 5):
    if min(lista) == lista[c]:
        print(c, end="... ")