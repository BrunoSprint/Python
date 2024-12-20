# Filtrar lista: Obter apenas os números pares
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  # Inclui apenas números pares
print(pares)  # Saída: [30, 2, 34]

# Modificar valores: Calcular o quadrado de cada número
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]  # Eleva cada número ao quadrado
print(quadrado)  # Saída: [1, 900, 441, 4, 81, 4225, 1156]


"""Conclusão
Compreensão de Listas:

É uma técnica essencial para manipular coleções de forma elegante e eficiente.
Ideal para filtrar e transformar dados em listas.
Aplicação Prática:

Amplamente utilizada em processamento de dados, filtragem de informações, e construção de coleções derivadas de forma compacta e legível."""