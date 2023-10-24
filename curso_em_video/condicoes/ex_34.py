#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1250 calcule um aumento de 10%
#para os inferiores ou iguais, o aumento e de 15%

salario = float(input("insira o valor do salario: "))

if(salario >1250):
    salario = salario * 1.1
else:
    salario = salario * 1.15

print("salario final = {}".format(salario))
