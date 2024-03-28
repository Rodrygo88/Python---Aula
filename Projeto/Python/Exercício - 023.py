print("====== DESAFIO 023 ======")
numero = int(input("Digite um número entre 0 e 9999: "))
u = numero // 1 % 10
c = numero // 10 % 10
d = numero // 100 % 10
m = numero // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(c))
print("Centena: {}".format(d))
print("Milhar: {}".format(m))