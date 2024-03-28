print("====== DESAFIO 068 ======")

import random

vitorias = 0

while True:
    escolha = str(input("Escolha Par ou Ímpar: P/I ")).strip().upper()[0]
    num = int(input("Digite o seu número de 0 a 10: "))
    print("=======================")

    if escolha in "P":
        escolhaPC = "I"
    elif escolha in "IÍ":
        escolhaPC = "P"
    
    numPC = random.randint(0, 10)
    soma = num + numPC
    
    teste =  soma%2

    resposta = ""

    print(f"A maquina ficou então com o {escolhaPC} e escolheu o número {numPC}!")
    print(f"A soma deu {soma}!")
    print("=======================")

    if teste == 1:
        resposta = "I"
    else: 
        resposta = "P"

    if resposta == escolha:
        print("Você GANHOU!!! Vamos de novo!")
        vitorias += 1
    else:
        print(f"Você PERDEU! Mas ganhou no total {vitorias} vezes!")
        break