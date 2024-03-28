print("====== DESAFIO 057 ======")

sexo = str(input("Sexo: (M) ou (F) ")).strip().upper()[0]

while sexo not in "MF":
    sexo = str(input("Opção ERRADA!!! Sexo: (M) ou (F) ")).strip().upper()[0]

print(f"Sexo: {sexo}")