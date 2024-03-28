print("====== DESAFIO 042 ======")

num1 = float(input("Reta 01: "))
num2 = float(input("Reta 02: "))
num3 = float(input("Reta 03: "))

menor1 = 0
menor2 = 0
maior = 0

if num1 >= num2 and num1 >= num3:
    menor1 = num2
    menor2 = num3
    maior = num1

else:
    if num2 >= num1 and num2 >= num3:
        menor1 = num1
        menor2 = num3
        maior = num2
    else:
        menor1 = num1
        menor2 = num2
        maior = num3

soma = menor1 + menor2

if soma > maior:

    print("É possivel SIM fazer um triângulo!!!")
    
    if num1 == num2 and num1 == num3:
        print("O triângulo é EQUILÁTERO!")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("O triângulo é ESCALENO!")
    else:
        print("O triângulo é ISÓCELES!")

else:
    print("NÃO é possivel fazer um triângulo...")