#parametros opcionais
def somar(a, b, c=0):
    s = a + b + c
    return(s)

print(somar(1, 3))

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Insira um numero:'))
if par(num):
    print('eh par')
else:
    print('nao eh par')