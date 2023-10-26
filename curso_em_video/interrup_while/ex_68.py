import random
# faca um programa que jogue par ou impar com o computador. o jogo so sera interrompido quando o jogador perder. mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
index = 0
while True:
    print('=-'*15)
    print('     PAR OU IMPAR')
    print('=-'*15)
    valor = int(input('diga um valor: '))
    pessoa = str(input('par ou impar? ')).strip().lower()
    pc = random.randint(1, 2)
    soma = valor + pc
    verifica = (soma) % 2
    if verifica == 0:
        resultado = 'par'
    elif verifica != 0:
        resultado = 'impar'
    print(f'tu jogou {valor} e o computador {pc}. total deu {soma} e DEU {resultado.upper()}')
    if resultado != pessoa:
        print('VOCE PERDEU')
        print('=-'*15)
        break
    if resultado == pessoa:
        index += 1
        print('VOCE VENCEU')
        print('=-'*15)
    print('vamos jogar novamente...')

print(f'game over! tu venceu {index} vezes')