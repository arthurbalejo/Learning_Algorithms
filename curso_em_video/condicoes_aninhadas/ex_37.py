#escreva um progama que leia um numero inteiro qaulquer e peca para o usuario escolher qual sera a base de conversao:
# 1 para binario
# 2 para octal
# 3 para

menu = int(input("digite: \n1 - binario\n2 - octal\n3 - hexa\n"))

numeroDecimal = int(input("digite o numero a ser convertido: "))

if(menu == 1):
    numeroConvertido = bin(numeroDecimal)
elif(menu == 2):
    numeroConvertido = oct(numeroDecimal)
else:
    numeroConvertido = hex(numeroDecimal)

print("numero convertido = {}".format(numeroConvertido))
