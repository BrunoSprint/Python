# Sistema de saque em diferentes tipos de contas bancárias

# Configurações do tipo de conta
conta_normal = False
conta_universitaria = False
conta_especial = True

# Configurações financeiras
saldo_disponivel = 2000  # Saldo atual na conta
valor_saque = 1500       # Valor solicitado para saque
limite_cheque_especial = 450  # Limite adicional do cheque especial

# Lógica para processamento do saque
if conta_normal:
    print("Conta normal selecionada.")
    # Verifica se o saldo é suficiente para o saque
    if saldo_disponivel >= valor_saque:
        print("Saque realizado com sucesso!")
    # Verifica se o cheque especial cobre o saque
    elif valor_saque <= (saldo_disponivel + limite_cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    # Caso nenhum dos dois seja suficiente
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

elif conta_universitaria:
    print("Conta universitária selecionada.")
    # Verifica se o saldo é suficiente para o saque
    if saldo_disponivel >= valor_saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

elif conta_especial:
    print("Conta especial selecionada.")
    # (Aqui pode-se adicionar lógica específica para contas especiais, se necessário)

else:
    # Caso o tipo de conta não seja identificado
    print("Sistema não reconheceu seu tipo de conta. Entre em contato com o seu gerente.")

