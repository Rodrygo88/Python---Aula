print("====== DESAFIO 034 ======")
sal = float(input("Salário: R$"))

if sal >= 1250:
    print("Seu salário com 10% de aumento ficou de R${}".format(sal+sal*0.10))
else:
    print("Seu salário com 15% de aumento ficou de R${}".format(sal+sal*0.15))
