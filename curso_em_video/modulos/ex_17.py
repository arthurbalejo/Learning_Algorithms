import math
#faca um prgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. calcule e omstre o comprimento da hipotenusa

co = float(input("Insira cateto oposto:"))
ca = float(input("Insira adjacente oposto:"))

hi = math.hypot(co, ca)

print("hipotenusaa = {:.2f}".format(hi))