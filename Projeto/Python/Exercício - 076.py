print("====== DESAFIO 076 ======")  

tupla = ("Lápis", 1, "Borracha", 2, "Caderno", 15.90, "Estojo", 25, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print("=========================================")
print(" ")

for c in range(0, len(tupla), 2):
    print(f"{tupla[c]:.<20} R$ {tupla[c+1]:>10.2f}")

print(" ")
print("=========================================")