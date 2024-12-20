# Lista de carros
carros = ["gol", "celta", "palio"]

# Iteração simples sobre os elementos da lista
for carro in carros:
    print(carro)  # Exibe cada carro da lista

# Iteração com índices e elementos usando enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")  # Exibe o índice e o carro


"""Conclusão
Iteração sobre listas:

É uma das operações mais comuns ao manipular coleções de dados em Python.
Loops simples são ideais para processar os elementos diretamente.
A função enumerate é útil quando é necessário acessar tanto o índice quanto o elemento de uma lista.

O uso do for simplifica a manipulação de dados em listas.
O enumerate é especialmente útil em casos onde é necessário rastrear a posição de cada elemento durante a iteração.

"""