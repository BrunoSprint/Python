# Demonstrando conversões de tipos e operações matemáticas

# Conversões de tipos numéricos
float_number = 1.97348728
print("Convertendo float para int (trunca o valor):", int(float_number))

string_number = "10"
print("Convertendo string para int:", int(string_number))

string_float = "10.10"
print("Convertendo string para float:", float(string_float))

integer_number = 100
print("Convertendo int para float:", float(integer_number))

# Conversão de inteiro para string e verificação de tipos
value = 10
value_as_string = str(value)

print("Tipo original da variável 'value':", type(value))
print("Tipo após conversão para string:", type(value_as_string))

# Operações matemáticas
divisao_normal = 100 / 2
divisao_inteira = 100 // 2

print("Resultado da divisão normal (float):", divisao_normal)
print("Resultado da divisão inteira (floor division):", divisao_inteira)
