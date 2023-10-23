#faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e a tangente desse angulo

import math
angulo = float(input("Insira um angulo: "))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print("seno = {:.2f}, cossseno = {:.2f} e tangente = {:.2f}".format(seno, cosseno, tangente))