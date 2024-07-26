print("====== DESAFIO 085 ======") 
 
numeros = [[],[]]

for c in range(0, 7):
    valor = int(input("Número: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print(numeros)

print(f"Pares: ", sorted(numeros[0]))
print(f"Impares: ",sorted(numeros[1]))