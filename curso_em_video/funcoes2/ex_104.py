#crie um programa que tenha a função leiaint(, qye vai funcionar de forma semelhante a função input do pytohn, só que fazenfo a validaçao
#para aceitar apenas um valor numerico

def leiaint(mensagem):
    dado = input(mensagem)
    while(dado.isnumeric() == False):
        print('\033[0;31mERRO! digite um numero valido\033[m')
        dado = input(mensagem)
    return(dado)
    

n = leiaint('digite um numero: ')
print(f'tu acabou de digitar o numero: {n}')