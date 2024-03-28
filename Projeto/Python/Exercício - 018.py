print("====== DESAFIO 018 ======")
import math
angulo = float(input("Digite o angulo: "))
rad = math.radians(angulo)
sen = math.sin(rad)
cos= math.cos(rad)
tan = math.tan(rad)
print("O angulo {:.2f} tem o seu SENO de {:.2f} seu COSSENO de {:.2f} e a sua TANGENTE de {:.2f} ".format(angulo, sen, cos, tan))