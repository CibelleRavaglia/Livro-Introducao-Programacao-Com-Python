"""
Escreva um programa que leia três números e que imprima o maior e o menor
"""
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informa o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print(f"\033[1;36;40mO menor número digitado foi {menor}.\033[m")
print(f"\033[1;36;40mO maior número digitado foi {maior}.\033[m")