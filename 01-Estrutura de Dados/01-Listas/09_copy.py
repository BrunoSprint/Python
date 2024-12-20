# Cria uma lista com elementos de diferentes tipos
lista = [1, "Python", [40, 30, 20]]

# Cria uma cópia superficial da lista
lista.copy()

# Exibe a lista original após a cópia
print(lista)  # Saída: [1, "Python", [40, 30, 20]]


"""Conclusão
Método copy:

Cria uma cópia rasa da lista, permitindo duplicar a estrutura da lista sem alterar a original.
A cópia é útil quando você precisa de uma lista separada, mas com os mesmos elementos, mantendo a integridade da lista original.
Aplicação Prática:

Quando você precisa criar uma cópia de uma lista para manipulação sem afetar a lista original, o método copy é uma boa escolha.

"""