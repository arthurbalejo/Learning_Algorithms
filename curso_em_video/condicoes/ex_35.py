#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo

l1 = float(input("Insira o valor de l1: "))
l2 = float(input("Insira o valor de l2: "))
l3 = float(input("Insira o valor de l3: "))

#verifica l1
if(l1 > l2 + l3 or l2 > l1 + l3 or l3 > l2 + l1):
    print("nao forma um triangulo")
else:
    print("forma")