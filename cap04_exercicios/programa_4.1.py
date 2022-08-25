"""
Condição if: estrutura de decisão
"""
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
if a > b:
    print('\033[1;36;40mO primeiro valor é maior!\033[m')
if b > a:
    print('\033[1;95;40mO segundo valor é maior!\033[m')