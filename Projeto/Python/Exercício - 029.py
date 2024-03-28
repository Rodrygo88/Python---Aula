print("====== DESAFIO 029 ======")
km = float(input("Velocidade do carro em Km/h: "))

if km > 80:
    print("Sua velocidade está acima do permitido, você foi MULTADO!")
    multa = (km-80)*7
    print("Sua multa ficou de R${}".format(multa))
else:
    print("Velocidade dentro do permitido!")
