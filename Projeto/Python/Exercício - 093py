print("====== DESAFIO 093 ======") 

jogador = {}
gols = []
total = 0

jogador["nome"] = str(input("Nome do jogador: ")).strip()
partidas = int(input("Partidas jogadas: "))

for c in range(0, partidas):
    gol = int(input(f"Gols na partida {c}: "))
    total += gol
    gols.append(gol)

jogador["gols"] = gols
jogador["total"] = total

print(jogador)
print()

print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, v in enumerate(jogador["gols"]):
    print(f"    => Na partida {i}, fez {v} gols.")

print(f"Foi um total de {jogador['total']} gols.")    
