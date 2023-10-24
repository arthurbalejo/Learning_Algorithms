# faca um programa que leia um ano qualquer e mostre se ele e bossesxto

ano = int(input("insira um ano: "))
anoTexto = str(ano)

if(ano % 4 == 0):
    print("ano bissexto")
else:
    print("nao eh")
    