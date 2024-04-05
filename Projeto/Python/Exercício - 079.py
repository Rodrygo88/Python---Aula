print("====== DESAFIO 079 ======")  

lista = []

while True:
    
    valor = int(input("Digite um número: "))

    if valor in lista:
        print("Valor já existente na lista! Não adicionado...")
    else:
        lista.append(valor)
    
    opção = str(input("Quer continuar? S/N ")).strip().upper()[0]
    
    while opção not in "SN":
        opção = str(input("DE NOVO, quer continuar? S/N ")).strip().upper()[0]

    if opção == "N":
        break

print(f"Valores: {sorted(lista)}")