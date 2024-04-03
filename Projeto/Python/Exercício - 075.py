print("====== DESAFIO 075 ======")  

tupla = (int(input("Digite um número: ")), 
         int(input("Digite outro número: ")), 
         int(input("Digite mais um número: ")), 
         int(input("Digite o último número: ")))

print(tupla)

print("=========================================================")

print(f"O número 9 aparece {tupla.count(9)} vezes!")

if 3 in tupla:
    print(f"O valor 3 apareceu na posição {tupla.index(3)+1}")
else:
    print("Não tem o número 3.")

print("Os números pares foram: ", end="")
for num in tupla:
    if num%2 == 0:
        print(num, end=" ")
