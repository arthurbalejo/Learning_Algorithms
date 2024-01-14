#faça um programa que tenha uma função chamada escreva(). que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável
#ex: escreva('ola mundo!')
#saida: 
#~~~~~~~~~~~~~
# ola, mundo!
#~~~~~~~~~~~~~

def escreva(texto):
    tamanho = len(texto) + 2
    print('~'*tamanho)
    print(f'{texto}')
    print('~'*tamanho)

texto = str(input('escreva a mensagem que deseja exibir: '))
escreva(texto)
