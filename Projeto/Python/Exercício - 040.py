print("====== DESAFIO 040 ======")
nota1 = float(input("Nota 01: "))
nota2 = float(input("Nota 02: "))

media = (nota1 + nota2)/2

print(f"Media do aluno: {media}")

if media < 5:
    print("Aluno reprovado!")

elif media >= 5 and media < 7:
    print("Aluno recuperação")

else:
    print("Aluno aprovado!")