#faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#se ele ainda vai se alistar ao servico militar
#se e a hora de se alistar
#se ja passou do tempo de alistamento
#seu pprogra tambem devera mostrar o tempo que falta ou que passou do prazo

anoNascimento = int(input("insira a data de nascimento: "))

alistamento = 2023 - anoNascimento

if (alistamento < 18):
    print("ainda faltam {} anos para se alistar".format((alistamento-18)*-1))
elif(alistamento > 18):
    print("atrasou {} anos no alistamento".format(alistamento-18))
else:
    print("esta na hora de se alistar")
