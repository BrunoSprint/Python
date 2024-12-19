# Definindo algumas variáveis e um dicionário
nome = "Bruno"
idade = 30
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Bruno", "idade": 30}

# Usando o operador % para formatar a string
print("Nome: %s Idade: %d" % (nome, idade))  
# Saída: "Nome: Bruno Idade: 30"
# O %s substitui pelo valor da variável 'nome' e o %d pelo valor da variável 'idade'

# Usando o método format() para formatar a string
print("Nome: {} Idade: {}".format(nome, idade))  
# Saída: "Nome: Bruno Idade: 30"
# O método format coloca as variáveis nas chaves na ordem em que são passadas

# Usando a formatação por índice no método format()
print("Nome: {1} Idade: {0}".format(idade, nome))  
# Saída: "Nome: Bruno Idade: 30"
# As chaves {0} e {1} referenciam os argumentos passados ao format na ordem

# Usando a formatação por índice e repetição
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))  
# Saída: "Nome: Bruno Idade: 30 Nome: Bruno Bruno"
# O índice 1 (nome) é repetido para imprimir mais de uma vez

# Usando nomes de variáveis diretamente no método format()
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))  
# Saída: "Nome: Bruno Idade: 30"
# Os nomes de variáveis são passados diretamente para o método format

# Usando a formatação com nomes no método format()
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))  
# Saída: "Nome: Bruno Idade: 30 Bruno Bruno 30"
# Aqui as variáveis são referenciadas pelos nomes definidos no método format()

# Usando o dicionário para formatar a string
print("Nome: {nome} Idade: {idade}".format(**dados))  
# Saída: "Nome: Bruno Idade: 30"
# O operador ** passa os valores do dicionário diretamente como argumentos nomeados

# Usando f-strings para formatar a string (Python 3.6+)
print(f"Nome: {nome} Idade: {idade}")  
# Saída: "Nome: Bruno Idade: 30"
# As f-strings permitem inserir diretamente as variáveis dentro das chaves {}

# Usando f-strings com formatação de número (duas casas decimais)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")  
# Saída: "Nome: Bruno Idade: 30 Saldo: 45.44"
# O :.2f formata o saldo para exibir 2 casas decimais

# Usando f-strings com formatação de número (largura mínima de 10 caracteres e uma casa decimal)
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")  
# Saída: "Nome: Bruno Idade: 30 Saldo:      45.4"
# O :10.1f formata o saldo para ter 10 caracteres de largura, com 1 casa decimal
