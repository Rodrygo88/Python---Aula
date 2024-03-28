print("====== DESAFIO 033 ======")
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Terceiro número: "))


if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 <= num3:
        menor = num2
    else:
        menor = num3

else:
    if num2 >= num3:
        maior = num2
        if num1 <= num3:
            menor = num1
        else:
            menor = num3
    else:
        maior = num3
        if num1 <= num2:
            menor = num1
        else:
            menor = num2



print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))