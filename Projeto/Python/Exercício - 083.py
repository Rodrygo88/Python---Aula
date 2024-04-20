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


"""
###RESPOSTA AULA

expr = str(input("Digite a sua expressão: "))

pilha = []

for simb in expr:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) == 0:
    print("Válida!")
    
else:
    print("Inválida!")"""