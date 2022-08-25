"""
Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
Obs: Os números primos são os números naturais que podem ser divididos por apenas dois
fatores: o número um e ele mesmo.
Vamos conferir alguns exemplos:
O número 5 tem apenas dois divisores: o número um e ele mesmo

"""
n = int(input("Digite um número: "))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if n >= 1:
        print("2")
        p = 1
        y = 3
        while p < n:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                print(x)
                p = p + 1
            y = y + 2