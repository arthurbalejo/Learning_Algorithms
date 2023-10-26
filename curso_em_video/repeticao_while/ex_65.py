# crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. o programa deve pergutnar ao usuario se ele quer ou nao continuar a digitar valores.

quantidade = numero = somatorio = index = maior = menor = 0
resposta = str(input('voce quer inserir numeros [S/N]: '))

while resposta not in 'NnSs':
    resposta = str(input('digite uma resposta valida. voce quer inserir mais numeros [S/N]: '))
    
while resposta in 'Ss':
    quantidade += 1
    numeros = int(input('insira os numero: '))

    if index == 0:
        maior = numeros
        menor = numeros
        index += 1
    else:
        somatorio += numeros
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    resposta = str(input('voce quer inserir mais numeros [S/N]: '))

media = somatorio / quantidade

print('media entre valores = {}'.format(media))
print('maior eh {} e o menor {}'.format(maior,menor))

