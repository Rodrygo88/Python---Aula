print("====== DESAFIO 083 ======")  

expressao = str(input("Digite a sua expressão: ")).strip()

cont_abertos = 0
cont_fechados = 0

for digito in expressao:
    if digito == "(":
        cont_abertos += 1
    elif digito == ")":
        if cont_abertos > 0:  
            cont_fechados += 1
            cont_abertos -= 1  
        else:
            cont_fechados += 100  
            break

if cont_abertos == 0 and cont_fechados < 100:  
    print("Ok")
else:
    print("Erro")
