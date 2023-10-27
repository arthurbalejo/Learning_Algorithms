# crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista. caso o numero ja exista la dentro, ele nao sera adicionado. no final, serao exibidos todos os valoresunicos giditados, em ordem crescente.

lista = []

while True:
    numero = int(input('insira um valor: '))
    if numero not in lista:
        lista.append(numero)
        print('valor adicionado com sucesso...')
    condicao = str(input('tu quer continua? [S/N] ')).strip().lower()
    if condicao not in 'sn':
        condicao = str(input('tu quer continua? [S/N] ')).strip().lower()
    if condicao == 'n':
        break
print('-='*30)
lista.sort()
print(f'tu digitou os valores: {lista}')