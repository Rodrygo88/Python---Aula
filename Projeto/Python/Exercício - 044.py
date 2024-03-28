print("====== DESAFIO 044 ======")
preço = float(input("Preço da compra: R$"))

print("""
      OPEÇÕES DE PAGAMENTO!!!

      Opção 1:
      À VISTA DINHEIRO /CHEQUE. (10% OFF)

      Opção 2:
      À VISTA CARTÃO. (5% OFF)

      Opção 3:
      ATÉ 2x CARTÃO. (PREÇO NORMAL)

      Opção 4:
      ATÉ  3x ou mais CARTÃO. (20% de juros!)
      
      """) 

opção = int(input("Opção de pagamento: "))

if opção == 1:
    valor = preço-preço*0.10
    print(f"Valor com desconto de 10% a pagar: R${valor}")

elif opção == 2:
    valor = preço-preço*0.05
    print(f"Valor com desconto de 5% a pagar: R${valor}")

elif opção == 3:
    valor = preço
    print(f"Valor normal sem desconto a pagar: R${valor}")

elif opção == 4:
    valor = preço+preço*0.20
    print(f"Valor com juros de 20% a pagar: R${valor}")

else: 
    print("ERRO, opção errada!")