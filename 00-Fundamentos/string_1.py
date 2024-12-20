# Definindo a variável 'nome'
nome = "BrUnO"

# Converte todos os caracteres para maiúsculos
print(nome.upper())  # Saída: "BRUNO"

# Converte todos os caracteres para minúsculos
print(nome.lower())  # Saída: "bruno"

# Converte a primeira letra de cada palavra para maiúscula
print(nome.title())  # Saída: "Bruno"

# Definindo a variável 'texto' com espaços no início e fim
texto = "  Olá mundo!    "

# Exibe o texto original com um ponto no final
print(texto + ".")  # Saída: "  Olá mundo!    ."

# Remove os espaços à esquerda e à direita e adiciona um ponto
print(texto.strip() + ".")  # Saída: "Olá mundo!.", remove espaços extras

# Remove os espaços à direita e adiciona um ponto
print(texto.rstrip() + ".")  # Saída: "  Olá mundo!.", remove espaços à direita

# Remove os espaços à esquerda e adiciona um ponto
print(texto.lstrip() + ".")  # Saída: "Olá mundo!    .", remove espaços à esquerda

# Definindo a variável 'menu'
menu = "Python"

# Adiciona "####" antes e depois da string 'menu'
print("####" + menu + "####")  # Saída: "####Python####"

# Centraliza a string 'menu' em um espaço de 14 caracteres (preenchendo com espaços à esquerda e à direita)
print(menu.center(14))  # Saída: "   Python    "

# Centraliza a string 'menu' em um espaço de 14 caracteres, preenchendo com '#' ao invés de espaços
print(menu.center(14, "#"))  # Saída: "###Python###"

# Junta as letras da palavra 'menu' com "-" entre elas
print("-".join(menu))  # Saída: "P-y-t-h-o-n"
