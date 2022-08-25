"""
Escreva um programa que verifique se um número é palíndromo.
Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
"""
# Para resolver este problema, podemos usar strings, apresentadas na seção 3.4 do livro
# Veja que estamos lendo o número sem convertê-lo para int ou float,
# desta forma o valor de s será uma string
"""
s = input("Digite o número a verificar, sem espaços: ")
i = 0
f = len(s)-1  # posição do último caracter da string
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(f"{s} é palíndromo")
else:
    print(f"{s} não é palíndromo")
"""


# Solução alternativa, usando apenas inteiros
n = int(input("Digite o número a verificar:"))
# Com n é um número inteiro, vamos calcular sua quantidade de dígitos,
# encontrado a primeira potência de 10, superior a n.
# Exemplo: 341 - primeira potência de 10 maior: 1000 = 10 ^ 4
# Utilizaremos 4 e não 3 para possibilitar o tratamento de números
# com um só dígito. O ajuste é feito nas fórmulas abaixo
q = 0
while 10 ** q < n:
    q = q + 1
i = q
f = 0
nf = ni = n  # Aqui nós copiamos n para ni e nf
pi = pf = 0  # e fazemos pi = pf (para casos especiais)
while i > f:
    pi = int(ni / (10 ** (i-1)))  # Dígito mais à direita
    pf = nf % 10                  # Dígito mais à esquerda
    if pi != pf:  # Se são diferentes, saímos
        break
    f = f + 1  # Passamos para o próximo dígito a esqueda
    i = i - 1  # Passamos para o dígito a direita seguinte
    ni = ni - (pi * (10 ** i))  # Ajustamos ni de forma a retirar o dígito anterior
    nf = int(nf / 10)  # Ajustamos nf para retirar o último dígito

if pi == pf:
    print(f"{n} é palíndromo")
else:
    print(f"{n} não é palíndromo")