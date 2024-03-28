print("====== DESAFIO 066 ======")

soma = 0
cont = -1

while True:
    num = int(input("Digite um número para somar: (999 para finalizar) "))
    cont += 1
    
    if num == 999:
        break
    else: 
        soma += num

print(f"Foram digitados {cont} números e a soma de todos eles é de {soma}!")
