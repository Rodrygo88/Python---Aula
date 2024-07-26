print("====== DESAFIO 089 ======") 

alunos = []

while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 01: "))
    nota2 = float(input("Nota 02: "))

    media = (nota1 + nota2) /2

    aluno = [nome, [nota1, nota2], media]

    alunos.append(aluno)

    opção = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if opção == "N":
        break

print("No. NOME      MÉDIA")
print("--------------------")
for i, c in enumerate(alunos):
    print(f"{i:<3}  {c[0]:^10}  {c[2]:^5.1f}")

print("--------------------")

while True:
    mostrar = int(input("Mostrar a nota de qual aluno? (999 interrompe) "))
    if mostrar == 999:
        break
    
    print(f"Notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}")