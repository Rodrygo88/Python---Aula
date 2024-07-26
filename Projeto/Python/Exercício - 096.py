print("====== DESAFIO 096 ======") 

def area(largura, comprimento):
    print(f"Área do terreno {largura:.1f}x{comprimento:.1f} é de {largura*comprimento:.1f}m².")


lar = float(input("LARGURA (m): "))
com = float(input("COMPRIMENTO (m): "))

area(lar, com)
