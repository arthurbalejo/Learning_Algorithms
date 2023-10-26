# escreva um progra,a que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci

n = int(input("insira os quantos eles tu quer mostrar: "))
c = 1
primeiro = 1
segundo = 1
termo = 0

while c < n :
    if c == 1:
        print("{} --> {} --> ".format(primeiro, segundo), end = '')
        c += 1
    elif c > 1:
        termo = primeiro + segundo
        primeiro = segundo
        segundo = termo
        print("{} --> ".format(termo), end = '')
        c += 1
