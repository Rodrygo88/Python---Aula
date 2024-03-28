print("====== DESAFIO 036 ======")
casa = float(input("Valor da casa: R$"))
salario = float(input("Salário mensal: R$"))
anos = int(input("Anos de financiamento: "))

meses = anos*12
valor_mes = casa/meses

porcento = salario*0.30

if porcento > valor_mes:
    print(f"A casa de R${casa:.2f} em {anos} anos a prestação será de R${valor_mes:.2f}!")
    print("Financiamento ACEITO!!!")
else:
    print(f"A casa de R${casa:.2f} em {anos} anos a prestação será de R${valor_mes:.2f}!")
    print("Financiamento NEGADO!")