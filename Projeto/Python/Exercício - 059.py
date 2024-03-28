print("====== DESAFIO 059 ======")


valor1 = float(input("Primeiro VALOR: "))
valor2 = float(input("Segundo VALOR: "))

opção = 0

while opção != 5:
    print("""
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
          """)
    
    opção = int(input("Escolha a opção desejada: "))
    if opção == 1:
        print(f"O resultado da SOMA entre {valor1} e {valor2} é igual a {valor1+valor2}.")

    elif opção == 2:
        print(f"O resultado da MULTIPLICAÇÂO entre {valor1} e {valor2} é igual a {valor1*valor2}.")

    elif opção == 3:
        if valor1 == valor2:
            print(f"O dois valores são iguais: {valor1} e {valor2}.")
        elif valor1 > valor2:
            print(f"O maior valor é o {valor1}.")
        elif valor1 < valor2:
            print(f"O maior valor é o {valor2}.")
    
    elif opção == 4:
        print("Digite os novos valores: ")
        valor1 = float(input("Primeiro VALOR: "))
        valor2 = float(input("Segundo VALOR: "))
    
    else:
        print("Opção errada, tente novamente!")

print("FIM DO PROGRAMA!!!")