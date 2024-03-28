print("====== DESAFIO 065 ======")

opção = "S"

cont = 0
soma = 0

maior = 0
menor = -1

while opção == "S":
    num = int(input("Digite um número: "))
    soma = num+soma
    cont += 1

    if num > maior:
        maior = num
    
    if cont == 1:
        menor = num
    else:
        if num < menor:
            menor = num
    
    
    opção = str(input("Quer continuar? (S/N) ")).strip().upper()
    if opção == "N":
        
        media = soma/cont

print(f"A média entre todos os {cont} números digitados é de {media:.2f}!")
print(f"A maior número é o {maior} e o menor número é o {menor}.")

