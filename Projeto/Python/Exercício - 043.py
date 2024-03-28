print("====== DESAFIO 043 ======")
altura = float(input("Altura: "))
peso = float(input("Peso: (Kg) "))

imc = peso / (altura * altura)

print(f"Seu IMC é de {imc:.1f}!")

if imc < 18.5:
    print("Seu PESO está ABAIXO DO PESO.")

elif imc < 25:
    print("Seu PESO está no PESO IDEAL!")

elif imc < 30:
    print("Seu PESO está em SOBREPESO.")

elif imc < 40:
    print("Seu PESO está em OBSEDIDADE.")

elif imc >= 40:
    print("Seu PESO está em OBSEDIDADE!!!")