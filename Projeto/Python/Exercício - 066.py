print("====== DESAFIO 066 ======")

soma = cont = 0 

while True:
    num = int(input("Digite um número para somar: (999 para finalizar) "))
    if num == 999:
        break
    
    soma += num
    cont += 1

print(f"Foram digitados {cont} números e a soma de todos eles é de {soma}!")
