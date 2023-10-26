#as tuplas sao imutaveis durante a execucao do programa
#identificadas por (), mas nao e mais necessario por
#lanche = 'hamburger', 'suco', 'pizza', 'pudim' pode ser assim a partir do python 3.6
#na hora de referenciar eh sempre conchetes
lanche = ('hamburger', 'suco', 'pizza', 'pudim')
#-2
print(f'-2: {lanche[-2]}')
#-1
print(f'-1: {lanche[-1]}')
#0
print(f'0: {lanche[0]}')
#3
print(f'3: {lanche[3]}')
#elemento 1 ate o 3, o ultimo nunca conta
print(lanche[1:3])
#inicio ate o elemento 2, o ultimo nunca conta
print(lanche[:2])
#inicio ate o elemento 2, o ultimo nunca conta
print(lanche[-2:])
#ler ao contrario
print(lanche[::-1])
#ler ao contrario de dois em dois
print(lanche[::-2])
#c armazena o item da tupla
for c in lanche:
    print(f'eu vou comer {c}')
print('-'*30)
#c armazena o index
for c in range(len(lanche)):
    print(f'eu vou comer {lanche[c]} na posicao {c}')
print('-'*30)
#c armazena o item e i o index
for i, c in enumerate(lanche):
    print(f'eu vou comer {c} na posicao {i}')

#ordem alfabetica e transforma em lista, mas nao muda
print(sorted(lanche))

#concatenacao de tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
#quantas vezes aparece o numero 5 na tupla
print(c.count(5))
#ver a posicao do elemento e pega a primeira ocorrencia
print(c.index(8))
#ver a posicao do elemento a partir de tal posicao
print(c.index(5,2))
#da pra armazer numeros e strings
pesssoa = ('arthur', 23, 'M', 68.5)
print(pesssoa)
pesssoa2 = ('arthur', 23, 'M', 68.5)
#apaga tupla
#del(pesssoa2)
print(pesssoa)