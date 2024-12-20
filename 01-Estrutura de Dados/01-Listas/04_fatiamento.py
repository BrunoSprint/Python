# Lista base
lista = ["p", "y", "t", "h", "o", "n"]

# Fatiamento a partir do índice 2 até o final
print(lista[2:])  # Saída: ["t", "h", "o", "n"]

# Fatiamento do início até o índice 2 (exclusivo)
print(lista[:2])  # Saída: ["p", "y"]

# Fatiamento do índice 1 até o índice 3 (exclusivo)
print(lista[1:3])  # Saída: ["y", "t"]

# Fatiamento do índice 0 ao índice 3 (exclusivo), pulando 2
print(lista[0:3:2])  # Saída: ["p", "t"]

# Fatiamento completo (copia toda a lista)
print(lista[::])  # Saída: ["p", "y", "t", "h", "o", "n"]

# Fatiamento completo com passo negativo (inverte a lista)
print(lista[::-1])  # Saída: ["n", "o", "h", "t", "y", "p"]


"""Conclusão
Fatiamento de Listas:

Permite acessar partes específicas da lista de forma eficiente.
Oferece flexibilidade ao manipular coleções de dados, como copiar, inverter ou selecionar elementos com base em critérios específicos.
Prática Essencial:

O fatiamento é uma habilidade essencial ao trabalhar com listas, strings e outros iteráveis em Python."""