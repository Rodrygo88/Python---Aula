print("====== DESAFIO 022 ======")

nome = str(input("Digite seu nome completo: ")).strip()

espaços = nome.count(" ")
letras = len(nome)
dividir = nome.split()

print("Maiúsculo:", nome.upper())
print("Minúscula:", nome.lower())
print("Tem {} letras.".format(letras-espaços))
print("{} é o primeiro nome e tem {} letras.".format(dividir[0], len(dividir[0])))
    