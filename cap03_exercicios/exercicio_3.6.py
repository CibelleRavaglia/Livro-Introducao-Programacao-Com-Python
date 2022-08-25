# Livro Introdução à Programação com Pyhton de Nilo Ney
"""
Exercício 3.6

Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada
nas seguintes variáveis: materia1, materia2, materia3.

"""
materia1 = 8
materia2 = 9
materia3 = 8
if materia1 > 7 and materia2 > 7 and materia3 > 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Infelizmente, você foi reprovado. Estude mais da próxima!')

## Na prática, o aluno é aprovado se obtiver nota maior ou igual a média, logo:
# materia1 >= 7 and materia2 >= 7 and materia3 >= 7