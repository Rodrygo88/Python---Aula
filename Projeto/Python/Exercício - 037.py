print("====== DESAFIO 037 ======")
num = int(input("Número inteiro: "))

print("CONVERTER!")
print("1 para binário")
print("2 para octal")
print("3 para hexadecimal")

escolha = int(input("Opção: "))

if escolha == 1:
    print(f"Binário: {bin(num)[2:]}")

elif escolha == 2:
    print(f"Octal: {oct(num)[2:]}")

elif escolha == 3:
    print(f"Hexadecimal: {hex(num)[2:]}")
else:
    print("Opção errada, tente novamente!")