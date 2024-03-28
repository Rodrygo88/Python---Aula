print("====== DESAFIO 060 ======")
num = int(input("Valor: "))
cont = num
resultado = num
while cont > 0:
    cont -= 1
    if cont != 0:
        resultado = resultado * cont
print(f"O fatorial de {num}! é {resultado}")