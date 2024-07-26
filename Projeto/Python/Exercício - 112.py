print("====== DESAFIO 112 ======")


import ex112.utilidades.moeda.moeda
import ex112.utilidades.dado.dado

p = ex112.utilidades.dado.dado.leiaDinheiro("Preço R$")

ex112.utilidades.moeda.moeda.resumo(p, 35, 22)


