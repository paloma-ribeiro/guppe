"""
Dictionary Comprehension

Criação de listas:
lista = [1, 2, 3, 4]

Criação de tupla:
tupla = (1, 2, 3, 4) ou tupla = 1, 2, 3, 4

Criação de set (conjunto):
conjunto = {1, 2, 3, 4}

Criação de dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe
{chave: valor for valor in iteravel}
"""
# Exemplos

# 1:
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# 2:
numeros = [1, 2, 3, 4, 5]
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# 3:
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com lógica condicional
numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
