print("====== DESAFIO 063 =====")

print("=== Sequência de Fibonacci ===")

num = int(input("Quantos elementos deseja ver? "))

valor1 = 1
valor2 = 1
soma = 0

cont = 0

if num == 1:
    print("0 ->")
if num == 2:
    print("0 -> 1 ->")
if num == 3:
    print("0 -> 1 -> 1 ->")
    
if num > 3:
    print("0 -> 1 -> 1 ->", end=" ")
    num = num-3

    while cont < num:

        cont += 1

        soma = valor1 + valor2
        if valor1 == valor2:
            valor2 = soma
        else:
            valor1 = valor2
            valor2 = soma
        
        print(f"{soma} -> ", end=" ")

print("FIM!")