# crie um programa que leia varios numeros inteiros pelo teclado. o programa so vai parar quando o usuario digitar 999, que a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles. (desconsiderando o flag)
#vou usar como exemplo pro break tambem
numero = somatorio = quantidade = 0


while numero != 999:
    numero = int(input("digite um numero: "))
    if numero == 999:
        break
    somatorio += numero
    quantidade +=1


print(f'somatorio = {somatorio} e quantidade de numeros = {quantidade}')
print('terminou!!!')