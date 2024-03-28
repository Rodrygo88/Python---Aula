print("====== DESAFIO 045 ======")

import random

print("JOKENPÔ!")

print("=========================")
print("""
      PEDRA 
      PAPEL
      TESSOURA
      """)
print("=========================")

escolha = str(input("Escolha: ")).strip().upper()

### PEDRA = 1 PAPEL = 2 TESSOURA == 3 ###

if escolha == "PEDRA":
    pc = random.randint(1,3)
    if pc == 1:
        print("EMPATOU, também escolhi PEDRA!")
    elif pc == 2:
        print("Você PERDEU, escolhi PAPEL!")
    elif pc == 3:
        print("Você GANHOU, escolhi TESSOURA!")

elif escolha == "PAPEL":
    pc = random.randint(1,3)
    if pc == 1:
        print("Você GANHOU, escolhi PEDRA!")  
    elif pc == 2:
        print("EMPATOU, também escolhi PAPEL!")
    elif pc == 3:
        print("Você PERDEU, escolhi TESSOURA!")

elif escolha == "TESSOURA":
    pc = random.randint(1,3)
    if pc == 1:
        print("Você PERDEU, escolhi PEDRA!")
    elif pc == 2:
        print("você GANHOU, escolhi PAPEL!")
    elif pc == 3:
        print("EMPATOU, também escolhi TESSOURA!")

else:
    print("A escolha não existe!")