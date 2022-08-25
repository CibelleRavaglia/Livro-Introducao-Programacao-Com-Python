"""
Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada:
2 x 1 = 2...
"""
n = int(input("Tabuada de:"))
x = 1
while x <= 10:
    print(f"{n} x {x} = {n * x}")
    x = x + 1