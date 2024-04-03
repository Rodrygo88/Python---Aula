print("====== DESAFIO 077 ======")  

tupla = ("aprender", "programar", "linguagem", "python", "curso", "gratis")

for palavra in tupla:
    print(f"Na palavra {palavra.upper()} temos: ", end="")

    for c in range(0, len(palavra)):
        if palavra[c] in "aeiou":
            print(palavra[c], end=" ")
    print("")