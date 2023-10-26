# crie um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. no final, mostre:
# A) quantas pessoas tem mais de 18 anos 
# b) quantos homente foram cadastrados
# c) quantas mulheres com menos de 20 anos foram cadastradas
somaIdade = 0
somaHomens = 0
somaI20 = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA'.center(30))
    print('-'*30)
    idade = int(input('Insira a idade: '))
    sexo = str(input('Sexo: [M/F] '))[0].upper()
    while sexo not in ('MmFf'):
        sexo = str(input('Sexo valido: [M/F] '))[0].upper()
    if idade > 18:
        somaIdade += 1
    if sexo == 'M':
        somaHomens += 1
    if sexo == 'F' and idade < 20:
        somaI20 += 1
    seguir = ''
    seguir = str(input('Quer continuar? [S/N] '))[0].upper()
    while seguir not in ('SsNn'):
        seguir = str(input('Quer continuar? [S/N] '))[0].upper()
    if seguir == 'N':
        break

print(f'A) quantas pessoas tem mais de 18 anos? {somaIdade}')
print(f'B) quantos homente foram cadastrados? {somaHomens}')
print(f'C) quantas mulheres com menos de 20 anos foram cadastradas? {somaI20}')
