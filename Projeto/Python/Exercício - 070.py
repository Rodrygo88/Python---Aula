print("====== DESAFIO 070 ======")

total = 0
cont_mil = 0
barato_preço = 0
barato_nome = ""

while True:
    nome_produto = str(input("Nome do produto: ")).strip().upper()
    preço = float(input("Preço do produto: R$"))

    total += preço

    if preço >= 1000:
        cont_mil += 1
    
    if barato_preço == 0:
        barato_preço = preço
        barato_nome = nome_produto
    else:
        if preço < barato_preço:
            barato_preço = preço
            barato_nome = nome_produto


    continuar = str(input("Comprar mais produtos? (S ou N) ")).strip().upper()[0]
    if continuar == "N":
        break

print(f"O total gasto é de R${total:.2f}")
print(f"Tem {cont_mil} produtos que custam mais de R$1000!")
print(f"{barato_nome} é o produto mais barato, custando R${barato_preço:.2f}!")