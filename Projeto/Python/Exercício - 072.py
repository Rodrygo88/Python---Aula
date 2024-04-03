print("====== DESAFIO 072 ======")

números = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

num = int(input("Número inteiro: (0 a 20) "))
while num < 0 or num > 20:
    num = int(input("Tente novamente! Número inteiro: (0 a 20 apenas) "))

print(f"O número escolhi foi {números[num]}.")