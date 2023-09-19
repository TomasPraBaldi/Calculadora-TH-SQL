valor1 = input("Digite o primeiro valor: ")
operador = input("Digite um operador matemático: + , - , / , ou *: ")
valor2 = input("Digite o segundo valor: ")


#NAO TA CERTO, NAO TA VALIDANDO O PRIMEIRO IF COMO TRUE...
if valor1.isdigit() or valor2.isdigit():
    print('digite um numero: ')
elif operador == "+":
    print(valor1+valor2)
elif operador == "-":
    print(valor1-valor2)
elif operador == "/":
    print(valor1/valor2)
elif operador == "*":
    print(valor1*valor2)
else:
    print("Digite algo valido.")


'''
value = input("Enter Value: ")
if value.isnumeric():
  print("Input value is Integer!")
else:
  print("Input value is Not an Integer!")
'''