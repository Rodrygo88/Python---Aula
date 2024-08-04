print("====== DESAFIO 113 ======") 

def leiaInt(texto="Digite um número inteiro: "):
      while True:
            try:
                  digito = int(input(texto))
            except:
                  print("ERRO")
            else:
                  break
      return digito

def leiaFloat(texto="Digite um número float: "):
      while True:
            try:
                  digito = float(input(texto)) 
            except:
                  print("ERRO")
            else:
                  break
      return digito
      
      


n = leiaInt("Digite um número inteiro: ")

n2 = leiaFloat("Digite um número float: ")

print(f"O número inteiro digitado foi o {n} e o float foi {n2}")