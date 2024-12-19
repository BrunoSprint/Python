# AND = para ser True, todas as condições têm que ser True
# OR = para ser True, apenas uma das condições precisa ser True

# AND entre condições, todas as condições precisam ser True
print(True and True and True)  # Retorna True, porque todas as condições são True
print(True and False and True)  # Retorna False, porque uma condição é False
print(False and False and False)  # Retorna False, porque todas as condições são False

# OR entre condições, basta uma condição ser True para o resultado ser True
print(True or True or True)  # Retorna True, porque pelo menos uma condição é True
print(True or False or False)  # Retorna True, porque uma condição é True
print(False or False or False)  # Retorna False, porque todas as condições são False

# Variáveis simulando uma operação bancária
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Expressão utilizando AND e OR para verificar se o saque pode ser realizado
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)  # Retorna True, porque uma das condições do OR é True

# Parênteses para controlar a ordem de avaliação
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)  # Retorna True, porque uma das condições do OR é True

# Condições separadas
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

# OR entre as condições de conta normal e conta especial
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)  # Retorna True, porque uma das condições é True
