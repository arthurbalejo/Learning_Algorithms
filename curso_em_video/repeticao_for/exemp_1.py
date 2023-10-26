for c in range(6): #zero a 5
    print("oi")
    print(c)
print("fim\n")

for c in range(1, 7): #1 a 6
    print("oi")
    print(c)
print("fim")

for c in range(0, 7, 2): #0 a 6 pulando de 2 em 2
    print("oi")
    print(c)
print("fim")

inicio = int(input("insira o numero inicial "))
fim = int(input("insira o numero final "))
passo = int(input("inssira o passo "))

for c in range(inicio, fim, passo):
    print(c)