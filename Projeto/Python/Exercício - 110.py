print("====== DESAFIO 110 ======")

from ex110 import moeda

p = float(input("Valor: R$"))

print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Aumentando 10% de {moeda.moeda(p)} é {moeda.aumentar(p, 10, True)}")
print(f"Diminuindo 13% de {moeda.moeda(p)} é {moeda.diminuir(p, 13, False)}")