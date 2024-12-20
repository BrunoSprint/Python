# Declaração de variáveis
produto_1 = 20
produto_2 = 10

# Operações matemáticas básicas
print("Adição:", produto_1 + produto_2)          # Soma de produto_1 e produto_2
print("Subtração:", produto_1 - produto_2)       # Subtração de produto_1 e produto_2
print("Divisão real:", produto_1 / produto_2)    # Divisão normal (resultado com casas decimais)
print("Divisão inteira:", produto_1 // produto_2) # Divisão inteira (resultado truncado)
print("Multiplicação:", produto_1 * produto_2)   # Multiplicação de produto_1 e produto_2
print("Módulo:", produto_1 % produto_2)         # Resto da divisão de produto_1 por produto_2
print("Exponenciação:", produto_1 ** produto_2) # produto_1 elevado à potência de produto_2

# Exemplos com precedência de operadores
x = (10 + 5) * 4  # Parênteses resolvidos primeiro, depois multiplicação
y = (10 / 2) + 25 * ((2 - 2) ** 2)  # Operações aninhadas com parênteses

print("Resultado de x:", x)  # Resultado da expressão para x
print("Resultado de y:", y)  # Resultado da expressão para y
