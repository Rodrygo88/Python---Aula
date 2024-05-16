print("====== DESAFIO 098 ======") 

import time

def contador(inicio, fim, passo):
    if inicio < fim:
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
        for c in range(inicio, fim+1, passo):
            print(c, end=" ")
            time.sleep(0.1)

    elif inicio > fim:
        if passo == -1:
            passo = 1
        if passo == 0:
            passo = 1
            
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
        for c in range(inicio, fim-1, -passo):
            print(c, end=" ")
            time.sleep(0.1)

    print("FIM!")
    print()


contador(1,10,1)

contador(10, 0, 2)

print("Agora pernozalize a contagem!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
pas = int(input("Passo: "))

contador(ini, fim, pas)
