def exibir_vogais():
    """
    Função que solicita um texto ao usuário e exibe apenas as vogais presentes no texto.
    """
    texto = input("Informe um texto: ")
    VOGAIS = "AEIOU"

    print("\nVogais presentes no texto informado:")
    for letra in texto:
        # Verifica se o caractere é uma vogal (maiúscula ou minúscula)
        if letra.upper() in VOGAIS:
            print(letra, end="")  # Exibe a vogal na mesma linha
    else:
        print()  # Adiciona uma quebra de linha após a exibição das vogais

def exibir_numeros():
    """
    Função que exibe os números de 0 a 50, em intervalos de 5.
    """
    print("\nNúmeros de 0 a 50 (em intervalos de 5):")
    for numero in range(0, 51, 5):
        print(numero, end=" ")  # Exibe os números na mesma linha, separados por espaços
    print()  # Adiciona uma quebra de linha ao final

# Chama as funções
exibir_vogais()
exibir_numeros()
