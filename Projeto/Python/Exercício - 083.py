print("====== DESAFIO 083 ======")  

expressão = str(input("Digite a sua expressão: ")).strip()

cont1 = 0
cont2 = 0

print(expressão)

for digito in expressão:

    if digito == "(":
        cont1 += 1
    else:
        if digito == ")":
            if cont1 >= cont2 and cont1 != 0:
                cont2 += 1
        


if cont1 == cont2:
    print("CORRETO!")

else:
    print("ERRADO!!!")
