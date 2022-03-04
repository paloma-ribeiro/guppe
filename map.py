"""
Map

Com map, é possível realizar o mapeamento de valores para função.
"""

import math


def area(r):
    """Calcula a área de um círculo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável.
# Retorna um Map Object

areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com Lambda
areas = map(lambda r: math.pi * (r ** 2), raios)
print(list(areas))

# OBS: após utilizar a função map(), depois da primeira utilização do resultado, ele zera.
