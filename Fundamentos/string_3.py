nome = "Bruno César Python Trial"

# Acessando o primeiro caractere da string
print(nome[0])  
# Saída: 'B'  
# O índice 0 corresponde ao primeiro caractere da string.

# Acessando o penúltimo caractere da string (índice -2)
print(nome[-2])  
# Saída: 'a'  
# O índice -2 refere-se ao penúltimo caractere da string.

# Fatiando da posição 0 até a posição 9 (sem incluir o caractere na posição 9)
print(nome[:9])  
# Saída: 'Bruno Cé'  
# O fatiamento vai de 0 até o índice 9 (sem incluir a posição 9).

# Fatiando da posição 10 até o final da string
print(nome[10:])  
# Saída: 'sar Python Trial'  
# O fatiamento começa na posição 10 e vai até o final da string.

# Fatiando da posição 10 até a posição 16 (não inclui o caractere na posição 16)
print(nome[10:16])  
# Saída: 'sar Pyt'  
# O fatiamento vai da posição 10 até 16 (sem incluir o caractere da posição 16).

# Fatiando da posição 10 até a posição 16, mas com um passo de 2
print(nome[10:16:2])  
# Saída: 'sr y'  
# O fatiamento começa na posição 10 e vai até a posição 16, mas pega de 2 em 2 caracteres.

# Fatiando a string toda
print(nome[:])  
# Saída: 'Bruno César Python Trial'  
# O fatiamento vai do começo ao fim da string.

# Invertendo a string
print(nome[::-1])  
# Saída: 'laiRT nihtyP raC onurB'  
# O fatiamento com passo -1 inverte a string.
