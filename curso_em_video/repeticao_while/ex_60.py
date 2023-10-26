# faca um programa que leia um numero qualquer e mostre o seu fatorial

numero = int(input('Insira um numero: '))
multiplicacao = 1

while numero > 0:
    print(numero)
    multiplicacao *= numero
    numero -= 1

print('fatorial eh: {}'.format(multiplicacao))