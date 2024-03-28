print("====== DESAFIO 017 ======")
import math
oposto = float(input("Cateto oposto: "))
adja = float(input("Cateto adjacente: "))
hipo = math.hypot(oposto,adja)
print("A hipotenusa é de {:.2f}".format(hipo))