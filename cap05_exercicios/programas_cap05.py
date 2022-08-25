#Contadores com while
"""
fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    print(x)
    x = x + 1
"""
#Um um número é par quando é zero ou múltiplo de 2
"""
fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x = x + 1
"""
#Forma mais simples
"""
fim = int(input('Digite o último número a imprimir: '))
x = 0
while x <= fim:
    print(x)
    x = x + 2
"""
"""
n = int(input('Tabuada de: '))
x = 1
while x <= 10:
    print(n + x)
    x = x + 1
"""
"""
pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f'Resposta da questão {questão}: ')
    if questão == 1 and resposta == 'b':
        pontos = pontos + 1
    if questão == 2 and resposta == 'a':
        pontos = pontos + 1
    if questão == 3 and resposta == 'd':
        pontos = pontos + 1
    questão = questão + 1
print(f' O aluno fez {pontos} ponto(s).')
"""
#While com acumuladores
"""
n = 1
soma = 0
while n <= 10:
    x = int(input(f'Digite o {n} número: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {soma}.')
"""
#Podemos definir a média aritmética como a soma de vários números divididos pela
#quantidade de números somados.
"""
x = 1
soma = 0
while x <= 5:
    n = int(input(f'{x} Digite o número: '))
    soma = soma + n
    x = x + 1
print(f'Média: {soma / 5:5.2f}')
"""
#Condição de parada while
"""
s = 0
while True:
    v = int(input('Digite um número a somar ou 0 para sair: '))
    if v == 0:
        break
    s += v
print(s)
"""
#Repetições aninhadas
#Combinação de vários while
"""
tabuada = 1
while tabuada <= 10:
    número = 1
    while número <= 10:
        print(f'{tabuada} x {número} = {tabuada * número}')
        número += 1
    tabuada += 1
"""
#F-strings
"""
a = 'mundo'
print(f'Alô, {a}!')
#Equivalente a "Alô %s" % a OU "Alô, {}".format(a)
a = 'mundo'
print('Alô, %s' % a)
"""
f"Preço: R${preço * 10:5.2f}!"
