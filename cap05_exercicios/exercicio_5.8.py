"""
Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro
pelo segundo. Utiliza apenas os operadores de soma e subtração para calcular o resultado.
Lembre-se de que podemos entender a multiplicação de dois números como soma sucessivas de
um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5

"""
p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print(f"{p} x {s} = {r}")