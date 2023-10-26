# faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' ou 'f'. caso esteja errado, peca a digitacao novamente ate ter um valor correto

sexo = str(input('Insira o sexo [M/F]: ')).strip().upper()

while sexo not in 'MmFf':
    sexo = str(input('Insira o sexo [M/F] noevamente: ')).strip().upper()

print(sexo)