"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Media: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter(),
# eles são excluídos da memória.

# Ex: removendo os espaços em branco
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, paises)

print(list(res))

# Exemplo mais complexo
usuarios = [
    {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'paloma', 'tweets': ['Eu amo cachorros', 'Vou sair hoje']},
    {'username': 'josue', 'tweets': []},
    {'username': 'beluga', 'tweets': ['Eu amo meu gato']}
]

# Filtrar os usuário que estão inativos no Twitter, de acordo com a lista acima.

# Forma 1:
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2:
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar filter() e map():
nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos
# de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
