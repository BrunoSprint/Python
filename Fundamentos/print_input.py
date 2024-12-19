# Solicita ao usuário que informe o nome e a idade
nome = input("Informe o seu nome: ")  # O valor digitado pelo usuário será armazenado na variável 'nome'
idade = input("Informe a sua idade: ")  # O valor digitado pelo usuário será armazenado na variável 'idade'

# Exibe o nome e a idade, separados por um espaço (padrão)
print(nome, idade)  # A saída será "nome idade" com um espaço entre eles

# Exibe o nome e a idade, mas o final da linha será "...", em vez da quebra de linha padrão
print(nome, idade, end="...\n")  # A saída será "nome idade..." com uma quebra de linha no final

# Exibe o nome e a idade, com o separador '#' entre as variáveis, e o final da linha será "..."
print(nome, idade, sep="#", end="...\n")  # A saída será "nome#idade..." com uma quebra de linha no final

# Exibe o nome e a idade, com o separador '#' entre as variáveis, mas sem o "..."
print(nome, idade, sep="#")  # A saída será "nome#idade" com a quebra de linha padrão ao final
