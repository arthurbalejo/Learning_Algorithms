frase = "Arthur carvalho Balejo"

print(frase[:6])
print(frase[16:])
print(frase[7:16:2])
print(frase[::3])
print(len((frase)))
#quantas letras o existem em frase
print(frase.count('o'))
print(frase.count('o', 0, 16))
#onde inicia a palavra que estou procurando
print(frase.find('car'))
print(frase.replace('Arthur', 'gremio'))
#maiuscula
print(frase.upper())
#minuscula
print(frase.lower())
#so a primeira maiuscula
print(frase.capitalize())
#iniciais das palavras maiusculas
print(frase.title())
#remover espaços no inicio e final das Strings
frase.strip()
#remover espaços no inicio e final das Strings DA DIREITA
frase.rstrip()
#remover espaços no inicio e final das Strings DA ESQUERDA
frase.lstrip()
#gera uma lista para cada palavra da cadeia de caracteres
print(frase.split())
fraseDividida = frase.split()
#mostrar item 2 da lista fraseDivida
print(fraseDividida[1])
#mostrar letra 3 do item 2 da lista fraseDivida
print(fraseDividida[1][3])
print(','.join(frase))
print('Arthur' in frase)
#string são imutáveios entao precisamos fazer uma nova atribuição para conseguir o resultado do replace

fraseSubst = frase.replace('Arthur','Gremio')
print(fraseSubst)
