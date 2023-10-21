def binary_search(list, item):
    baixo = 0
    alto = len(list) - 1
    
    while baixo <= alto:
       meio = (baixo + alto) // 2
       chute = list[meio]

       if chute == item:
        return meio
       
       if chute > item:
        alto = meio -1
    
       else:
        baixo = meio + 1

    return None

minha_lista = [1, 3, 5, 7, 9]
print (binary_search(minha_lista, 7)) # -> 1
print (binary_search(minha_lista, 1))
print (len(minha_lista))

    
