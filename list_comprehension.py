"""
List Comprehension

Utilizando List Comprehension nós podemos gerar novas listas com dados processados
a partir de outro iterável.

# Sintaxe da List Comprehension
[dado for dado in iterável]
"""

# Exemplos

numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

"""
Para entender o que está acontecendo, é necessário dividir a expressão em duas partes:
- Primeira parte: for numero in numeros
- Segunda parte: numero * 10
"""

res = [numero / 2 for numero in numeros]
print(res)

# List Comprehension versus Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

# Outros exemplos

# 1:
nome = 'Paloma Ribeiro'
print([letra.upper() for letra in nome])


# 2:
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'marcela', 'adão']

print([caixa_alta(amigo) for amigo in amigos])

# 3:
print([numero * 3 for numero in range(1, 10)])

# 4:
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5:
print([str(numero) for numero in [1, 2, 3, 4, 5]])

"""
Podemos adicionar estruturas condicionais lógicas as nossas List Comprehension
"""

# Exemplos

# 1:
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando a expressão acima

# Qualquer número par módulo de 2 é 0 e 0 em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número ímpar módulo de 2 é 1, e 1 em Python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2:
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
