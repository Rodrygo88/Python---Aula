print("====== DESAFIO 103 ======") 
 
def ficha(nome="<desconhecido>", gols="0"):
      
      return print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


jogador = str(input("Nome do Jogador: "))
quant_gols = str(input("Número de Gols: "))
if quant_gols.isnumeric():
      quant_gols = int(quant_gols)
else:
      quant_gols = 0


if len(jogador) ==  0:
      ficha(gols = quant_gols)

elif len(str(quant_gols)) ==  0:
      ficha(nome = jogador)
      
else:
      ficha(nome = jogador, gols = quant_gols)