"""
Set Comprehension

Set = {1, 2, 3, 4, 5}
"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Outros Exemplos:
letras = {letra for letra in 'Paloma Ribeiro'}
print(letras)
