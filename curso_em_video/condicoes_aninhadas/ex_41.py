# a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -ate 9 anos mirin
# -ate 14 anos infantil
# -ate 19 anos junior
# -ate 25 anos senior
# -acima master

n = int(input("insira a data de nascimento: "))

dataNascimento = 2023 - n

if(dataNascimento <= 9):
    print("mirin")
elif(dataNascimento <= 14):
    print("infantil")
elif(dataNascimento <= 19):
    print("junior")
elif(dataNascimento <= 25):
    print("senior")
else:
    print("master")