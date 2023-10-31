pessoas = {'nome':'Gustavo', 'sexo':'M','idade':22}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('*1'*30)

for k in pessoas.keys():
    print(k)

print('*2'*30)

for v in pessoas.values():
    print(v)

print('*3'*30)

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('*4'*30)

del pessoas['sexo']

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('*5'*30)

pessoas['nome'] = 'Leandro'

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('*6'*30)

pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('*'*30)