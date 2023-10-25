# refaca o desafio 35 dos triangulos, acrescentando o recuso de mostrar que tipo de triangulo sera formado:
# -equilatero: todos os lados iguais
# -isosceles: dois lados iguais
# -escalenoo: todos os lados diferentes

l1 = float(input("Insira o valor de l1: "))
l2 = float(input("Insira o valor de l2: "))
l3 = float(input("Insira o valor de l3: "))


if(l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1):
    #condicao aninhada
    if(l1 == l2 == l3):
        print("equilatero")
    elif(l1 == l2 or l2 == l3 or l1 ==l3):
        print("isosceles")
    else:
        print("escalno")
else:
    print("nao forma um triangulo")