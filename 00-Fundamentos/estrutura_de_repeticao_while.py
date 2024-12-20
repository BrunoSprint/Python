def exibir_menu():
    """
    Exibe o menu principal do sistema bancário.
    """
    print("\n--- Menu do Sistema Bancário ---")
    print("[1] Sacar")
    print("[2] Extrato")
    print("[0] Sair")
    return int(input("Escolha uma opção: "))

def processar_opcao(opcao):
    """
    Processa a escolha do usuário com base na opção informada.
    """
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    elif opcao == 0:
        print("Obrigado por usar nosso sistema bancário, até logo!")
    else:
        print("Opção inválida! Tente novamente.")

def main():
    """
    Função principal que controla o loop do menu interativo.
    """
    opcao = -1  # Inicializa com um valor diferente de 0 para entrar no loop
    while opcao != 0:
        try:
            opcao = exibir_menu()
            processar_opcao(opcao)
        except ValueError:
            print("Por favor, insira um número válido.")

# Executa o programa
main()
