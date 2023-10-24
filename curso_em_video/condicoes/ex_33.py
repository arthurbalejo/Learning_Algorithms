# faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor

n1 = int(input("insira um numero: "))
n2 = int(input("insira um numero: "))
n3 = int(input("insira um numero: "))
#verificando o menor
menor = n1

if(menor > n2):
    menor = n2

if(menor > n3):
    menor = n3

#verificando o maior
maior = n1

if(maior < n2):
    maior = n2

if(maior < n3):
    maior = n3

print("maior = {} e menor = {}".format(maior, menor))