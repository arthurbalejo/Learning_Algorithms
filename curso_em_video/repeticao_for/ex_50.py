#desenvolva um programa que leia seis numeros inteiros e mostre a soma daqueles que forem pares. se o valor digitado for impar desconsidere-o
soma = 0
for c in range (1, 7):
    numero = int(input("insira um numero: "))
    if(numero % 2 == 0):
        soma += numero

print(soma)