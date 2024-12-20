# Inicializa as variáveis
saldo = 1000  # Saldo da conta
limite = 1000  # Limite de crédito

# Verifica se saldo e limite referenciam o mesmo objeto na memória
print(saldo is limite)  # Verifica se saldo e limite são o mesmo objeto. Retorna False.

# Verifica se saldo e limite não referenciam o mesmo objeto na memória
print(saldo is not limite)  # Verifica se saldo e limite não são o mesmo objeto. Retorna True.
