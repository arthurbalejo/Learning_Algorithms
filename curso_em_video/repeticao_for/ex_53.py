#crie um programa que leia uma frase qualquer e diga se ela e um palindromo desconsiderando os espacos


frase = str(input("insira a frase: ")).strip().upper()

fraseSEspacos = frase.replace(" ", "")

#palavras = frase.split()
#unto = "".join(palavras)

print(len(fraseSEspacos))

fraseInvertida = ''

#modo alternativo super simples
#fraseInversa = fraseSEspacos[::-1]

for c in range (len(fraseSEspacos)-1, -1,-1):
    print(fraseSEspacos[c])
    fraseInvertida += fraseSEspacos[c]

print(fraseInvertida)
print(len(fraseInvertida))

if(fraseSEspacos == fraseInvertida):
    print("eh palindromo")
else:
    print("nao eh palindromo")