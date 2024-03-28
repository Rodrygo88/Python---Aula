print("====== DESAFIO 069 ======")

maior = 0
homens = 0
mulheres = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Seu sexo: (M ou F) ")).strip().upper()[0]

    if idade >= 18:
        maior += 1

    if sexo == "M":
        homens += 1

    if sexo == "F":
        if idade < 20:
            mulheres += 1

    continuar = str(input("Quer continuar? (S ou N)")).strip().upper()[0]

    if continuar == "N":
        break
        

print(f"Tem cadastradas {maior} pessoas com mais de 18 anos!")
print(f"Tem cadastados {homens} homens no total!")
print(f"Tem cadastradas {mulheres} com menos de 20 anos!")