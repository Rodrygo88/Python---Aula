print("====== DESAFIO 031 ======")
distancia = int(input("Distancia da viagem em Km/h: "))

if distancia <= 200:
    calculo = distancia*0.50
    print("Sua passagem vai custar R${:.2f}, custo por Km é de R$0.50 para até 200Km.".format(calculo))
else:
    calculo = distancia*0.45
    print("Sua passagem vai custar R${:.2f}, custo por Km é de R$0.45 para mais de 200Km.".format(calculo))