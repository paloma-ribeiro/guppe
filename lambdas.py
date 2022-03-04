"""
Utilizando Lambdas

Lambdas são funções sem nome, ou seja, funções anônimas.
"""


# Função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda:
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# É possível ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' paloma', 'RIbeiro'))
print(nome_completo(' palOmA', 'RIBEIRO'))

# Em funções Python, podemos ter nenhuma ou várias entradas, em Lambdas também.

exemplo = lambda: 'Python!'
print(exemplo())

# Outro Exemplo
# Ordenação pelo sobrenome com expressão lambda

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heilein', 'Arthur C. Clarke', 'Frank Herbert']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
