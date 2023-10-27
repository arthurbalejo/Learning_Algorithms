num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0) #na posicao 2 inserir o numero zero
#num.pop(2)
if 5 in num:
    num.remove(5)
else:
    print('nao achei o numero 5')
print(num)
print(f'essa lista possui {len(num)} elementos')

print('\n')
print('*'*30)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}', end='...')

print('\n')
print('*'*30)

for c, va in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {va}...')

