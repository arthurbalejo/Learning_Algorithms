 #crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo fatorial.

def fatorial(numero, show=False):
    n = 1

    if show == True:
        for c in range (numero, 0, -1):
            if c > 1:
                print(f'{c} * ', end='')
            else:
                print(f'{c} = ', end='')
            n *= c
        
        print(f'{n}')

    else:
        for c in range (numero, 0, -1):
            n *= c
    
        print(f'{n}')

fatorial(5, True)