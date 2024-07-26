print("====== DESAFIO 090 ======") 

aluno = {}

aluno["nome"] = str(input("Nome do aluno: ")).strip()
aluno["media"] = float(input("Média do aluno: "))

if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
else:
    aluno["situação"] = "Reprovado"

print(f"Nome é igual a {aluno['nome']}")
print(f"Média é igual a {aluno['media']}")
print(f"Situação é igual a {aluno['situação']}")