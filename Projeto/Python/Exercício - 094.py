print("====== DESAFIO 094 ======") 

lista_pessoas = []
total_idade = 0

while True:

    pessoa = {}
    pessoa["nome"] = str(input("Nome: ")).strip()
    while True:
        pessoa["sexo"] = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if pessoa["sexo"] in "MF":
            break
        print("Erro, escolha não disponivel! ")
        
    idade = int(input("Idade: "))
    pessoa["idade"] = idade

    total_idade += idade
    

    lista_pessoas.append(pessoa.copy())
    del pessoa

    while True:
        opção = str(input("Continuar? [S/N] ")).strip().upper()[0]
        if opção in "SN":
            break
        print("Erro, escolha não disponivel! ")
    if opção == "N":
        break
    
print(lista_pessoas)
print("======="*2)

print(f"- O grupo tem {len(lista_pessoas)} pessoas.")
print(f"- A média de idade é de {total_idade / len(lista_pessoas)} anos.")
print("- As mulheres cadastradas foram: ", end=" ")
for c in lista_pessoas:
    if c["sexo"] == "F":
        print(c["nome"], end=" ")

print()
print("- Lista das pessoas acima da média: ")
print()

for c in lista_pessoas:
    if c["idade"] > total_idade / len(lista_pessoas):
        print(f'Nome = {c["nome"]}; Sexo = {c["sexo"]}; Idade = {c["idade"]}; ')

print()
print("Fim...")