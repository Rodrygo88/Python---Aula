print("====== DESAFIO 053 ======")

frase = str(input("Escreva uma frase: ")).strip().split()
frase = "".join(frase)

inverso = ""

for c in range(len(frase)-1, -1, -1):
    inverso = inverso + frase[c] 

print(f"A frase '{frase}' invertida ficou como: '{inverso}'. ")
if frase == inverso:
    print("Temos um PALÍNDROMO!")

else:
    print("NÃO temos um PALÍNDROMO...")