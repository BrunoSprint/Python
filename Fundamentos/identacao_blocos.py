# Variável global para armazenar o saldo
saldo = 500

def sacar(valor):
    """
    Realiza a operação de saque, verificando se o valor está disponível no saldo.
    """
    global saldo  # Acessa a variável global de saldo
    if saldo >= valor:
        saldo -= valor
        print(f"Valor de {valor} sacado com sucesso!")
        print("Retire o seu dinheiro na boca do caixa.")
    else:
        print(f"Saldo insuficiente! Você tentou sacar {valor}, mas seu saldo é {saldo}.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!\n")

def depositar(valor):
    """
    Realiza a operação de depósito, adicionando o valor ao saldo.
    """
    global saldo  # Acessa a variável global de saldo
    saldo += valor
    print(f"Depósito de {valor} realizado com sucesso! Seu novo saldo é {saldo}.\n")

# Testando as funções
print(f"Saldo inicial: {saldo}\n")
sacar(1000)  # Tentativa de saque maior que o saldo
depositar(500)  # Depósito de 500
sacar(800)  # Saque válido
