print("====== DESAFIO 095 ======") 

lista = []

while True:
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

    lista.append(jogador.copy())

    opção = str(input("Continuar? [S/N] ")).strip().upper()[0]
    if opção == "N":
        break

print("=" * 40)
print(f"{'cod':<4}{'nome':<10}{'gols':<10}{'total':<10}")
print("=" * 40)

for i, d in enumerate(lista):
    print(f' {i:>2} {d["nome"].center(10)} {str(d["gols"]).center(10)} {str(d["total"]).center(10)}')

print()

while True:
    dados = int(input("Dados de qual jogador: (999 interromper) "))
    if dados == 999:
        break
    elif dados > len(lista)-1:
        print("jogador não existe, tente novamente")

    for i, jogador in enumerate(lista):
        if i == dados:
            print(f"LEVANTAMENTO DO JOGADOR {jogador['nome']}: ")
            for i, v in enumerate(jogador["gols"]):
                print(f"    No jogo {i}, fez {v} gols.")
            print()
            
print("Fim...")
