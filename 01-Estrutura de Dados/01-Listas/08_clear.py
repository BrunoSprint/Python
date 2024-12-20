# Cria uma lista com elementos de diferentes tipos
lista = [1, "Python", [40, 30, 20]]

# Exibe a lista original
print(lista)  # Saída: [1, "Python", [40, 30, 20]]

# Remove todos os elementos da lista
lista.clear()

# Exibe a lista após a operação de limpeza
print(lista)  # Saída: []


"""Conclusão
Método clear:

É útil quando queremos esvaziar uma lista sem recriar sua estrutura.
A lista permanece disponível para receber novos elementos após a operação.
Aplicação Prática:

Usado em cenários onde a mesma lista é reaproveitada para diferentes conjuntos de dados, como durante iterações em loops ou reinicialização de coleções em programas dinâmicos."""