print("====== DESAFIO 075 ======")  

tupla = (int(input("Digite um número: ")), 
         int(input("Digite outro número: ")), 
         int(input("Digite mais um número: ")), 
         int(input("Digite o último número: ")))

print(tupla)

cont_9 = 0

for num in tupla:
    if num == 9:
        cont_9 += 1

print("=========================================================")

print(f"O número 9 aparece {cont_9} vezes!")

for c in range(0, 4):
    if tupla[c] == 3:
        print(f"O primeiro valor 3 foi digitado na posição {c+1}.")
        break
    if c == 3:
        print("Não tem 3 na tupla!")

print("Os números pares foram: ", end="")
for num in tupla:
    if num%2 == 0:
        print(num, end=" ")
