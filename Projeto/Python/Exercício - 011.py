print("====== DESAFIO 011 ======")
alt = float(input("Altura da parede: "))
lar = float(input("Largura da parede: "))
area = alt*lar
tinta = area/2
print("A área da parede é de {} metros quadrados.".format(area))
print("Para pintar essa pareda vai precisar de {} litros de tinta.".format(tinta))