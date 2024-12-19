def processar_input():
    """
    Função que solicita ao usuário um número, verifica condições e exibe números ímpares.
    """
    while True:
        try:
            numero = int(input("Informe um número (Digite 10 para encerrar): "))

            # Interrompe o loop se o número for 10
            if numero == 10:
                print("Programa encerrado.")
                break

            # Ignora números pares
            if numero % 2 == 0:
                continue

            # Exibe números ímpares
            print(f"Número ímpar informado: {numero}")

        except ValueError:
            print("Por favor, insira um número válido.")

def exibir_impares():
    """
    Função que exibe números ímpares de 0 a 99.
    """
    print("\nNúmeros ímpares de 0 a 99:")
    for numero in range(100):
        # Ignora números pares
        if numero % 2 == 0:
            continue

        # Exibe números ímpares
        print(numero, end=" ")

# Chama as funções
processar_input()
exibir_impares()
