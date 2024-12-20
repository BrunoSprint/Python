def verificar_eligibilidade(idade):
    """
    Verifica a elegibilidade do usuário para tirar a CNH com base na idade.
    """
    MAIOR_IDADE = 18
    IDADE_ESPECIAL = 17

    if idade >= MAIOR_IDADE:
        print("Maior de idade, pode tirar a CNH.")
    elif idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
    else:
        print("Ainda não pode tirar a CNH.")

# Solicita a idade do usuário
try:
    idade_usuario = int(input("Informe sua idade: "))
    verificar_eligibilidade(idade_usuario)
except ValueError:
    print("Por favor, insira um número válido.")
