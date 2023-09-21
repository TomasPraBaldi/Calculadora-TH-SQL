valor1 = input("First value: ")
if valor1.isdigit(): 
    print()
else:
    print("This calculator can't use letters!")
operador = input("Operator: + , - , / , or *: ")
valor2 = input("Second value: ")
if valor2.isdigit():
    print()
else:
    print("This calculator can't use letters!")


#TENTATIVA 1 PRA DAR UMA MENSAGEM SE O USER DIGITAR STR
#if valor1.isdigit() or valor2.isdigit():
#    print('digite um numero: ')

#TENTATIVA 2 PRA DAR UMA MENSAGEM SE O USER DIGITAR STR
#if isinstance(True, (str)):
#   print('digite um numero: ')

if operador == "+":
    print(valor1+valor2)
elif operador == "-":
    print(valor1-valor2)
elif operador == "/":
    print(valor1/valor2)
elif operador == "*":
    print(valor1*valor2)
else:
    print("Digite um operador valido.")


'''
value = input("Enter Value: ")
if value.isnumeric():
    print("Input value is Integer!")
else:
    print("Input value is Not an Integer!")
'''