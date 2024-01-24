#crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório na eleições.

def voto(ano_nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - ano_nascimento

    if idade < 18:
        return f'{idade} anos tem voto negado'
    elif  18 <= idade < 70:
        return f'{idade} anos o voto eh obrigatório'
    else:
        return f'{idade} anos o voto eh facultatvo'
    
ano = int(input('insira teu ano de nascimento: '))

print(voto(ano))