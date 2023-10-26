# desenvolva um programa que leia o nome, idade e sexo de 4 pessoa. no final do programa mostre:
# a media de idade do grupo.
# qual o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

somaIdade = 0
nome = ('')
maiorIdadeHomem = 0
nomeVelho = ''
mulheresMenosVinte = 0

for c in range(1, 5):
    nome = str(input("insira a nome: ")).strip()
    idade = int(input("insira a idade: "))
    sexo = str(input("insira o sexo (m ou f): ")).strip().lower()
    somaIdade += idade

    if(c == 1 and sexo == 'm'):
        maiorIdadeHomem = idade
        nomeVelho = nome
    if(sexo == 'm' and idade > maiorIdadeHomem):
        maiorIdadeHomem = idade
        nomeVelho = nome
    if(sexo == 'f' and idade < 20):
        mulheresMenosVinte += 1


mediaIdade = somaIdade / 4
print ("media da idade do grupo eh: {}".format(mediaIdade))
print("o homem mais velho tem {} ano e se chama {}".format(maiorIdadeHomem, nomeVelho))
print("{} mulheres tem mais de 20 anos".format(mulheresMenosVinte))
