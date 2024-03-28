print("====== DESAFIO 067 ======")

while True:
    num = int(input("Digite um número inteiro: "))
    print("")
    if num < 0:
        print("Fim!")
        break
    for c in range(1, 11):
        print(f"{num} X {c} = {c*num}")
    print("")
    
