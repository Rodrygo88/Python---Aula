print("====== DESAFIO 056 ======")

idades = 0
velho = ""
idade_v = 0
mulheres = 0

for c in range(0, 4):
    nome = str(input(f"Nome da {c+1}º pessoa: ")).strip().upper()
    idade = int(input(f"Idade da {c+1}º pessoa: "))
    sexo = str(input(f"Sexo da {c+1}º pessoa: (M) ou (F) ")).strip().upper()

    print("====================================")

    idades += idade

    if c == 0:
        velho = nome
        idade_v = idade
    
    if idade > idade_v:
        velho = nome

    if sexo == "F":
        if idade < 20:
            mulheres += 1

media = idades/4

print(f"A média da idade de todos é de {media} anos.")
print(f"A pessa mais velha é {velho}!")
print(f"Tem {mulheres} mulheres com menos de 20 anos.")