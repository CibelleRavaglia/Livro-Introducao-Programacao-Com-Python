"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma, subtração, multiplicação e divisão.
Exiba o resultado da operação solicitada.

"""
#Minha solução
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informa o segundo número: '))
operação = str(input('Informe a operação que você quer realizar por extenso: '))
if operação == 'soma':
    operação = n1 + n2
elif operação == 'subtração':
    operação = n1 - n2
elif operação == 'multiplicação':
    operação = n1 * n2
elif operação == "divisão":
    operação = n1 / n2
else:
    print("Operações inválidas.")
    operação = 0

print('O resultado da operação é {}'.format(operação))

#Solução do livro
a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)
