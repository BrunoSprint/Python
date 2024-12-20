# Definição da matriz
matriz = [
    [1, "a", 2],  # Primeira sublista
    ["b", 3, 4],  # Segunda sublista
    [6, 5, "c"]   # Terceira sublista
]

# Acessando a primeira sublista inteira
print(matriz[0])  # Saída: [1, "a", 2]

# Acessando o primeiro elemento da primeira sublista
print(matriz[0][0])  # Saída: 1

# Acessando o último elemento da primeira sublista
print(matriz[0][-1])  # Saída: 2

# Acessando o último elemento da última sublista
print(matriz[-1][-1])  # Saída: "c"


"""Conclusão
Matrizes em Python:

Representadas como listas de listas, são úteis para organizar dados em estruturas bidimensionais.
Acessar elementos em uma matriz requer o uso de índices para identificar a sublista e o elemento desejado.
Índices Negativos:

Permitem acessar elementos de trás para frente, tanto nas sublistas quanto na matriz como um todo.
Essa abordagem é fundamental para manipular dados em estruturas mais complexas, como tabelas ou grids."""