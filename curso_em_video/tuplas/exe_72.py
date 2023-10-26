# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
# seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso
numero = 0
extenso = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Insira um numero: '))
    if 0 <= numero <= 20:
        print(f'tu digitou: {extenso[numero - 1]}')
        continuar = str(input('tu quer continuar? [S/N]')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('tu quer continuar? [S/N] (resposta invalida)')).strip().upper()
        if continuar == 'N':
            break
        else:
            numero = int(input('Insira um numero: '))
                
    numero = print('Tente novamente. ', end = '')
    

