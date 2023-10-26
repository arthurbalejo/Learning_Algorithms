# crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar 999, que a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles. (desconsiderando o flag)

numero = somatorio = quantidade = 0

numero = int(input("digite um numero: "))
while numero != 999:
    somatorio += numero
    quantidade +=1
    numero = int(input("digite um numero: "))

print('somatorio = {} e quantidade de numeros = {}'.format(somatorio, quantidade))
print('terminou!!!')