# crie um programa onde o usuario digite uma exppressao qualquer que use parenteses. seu aplicativo devera analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta

expressao = str(input('insira a expresssao: '))

expressaoP = []

for elemento in expressao:
    #verifico se o elemento eh '('
    if elemento == '(':
        #adiciono '(' na lista expressaoP
        expressaoP.append(elemento)
    #se o elemento for ')'
    elif elemento == ')':
        #e a lista expressaoP nao estiver vazia
        if len(expressaoP) > 0:
            #removo o ultimo elemento que eh um '('
            expressaoP.pop()
        #se a lista estiver vazia
        else:
            #adiciono ')' na lista expressaoP
            expressaoP.append(elemento)
            break #no momento em que ) foi colocado na pilha quebra o laco pois nao  precisa mais verificar
        
#caso tenha um elemento na lista expressaoP eh incorreto
if len(expressaoP) == 0:
    print('correto')
else:
    print('incorreto')