"""
TIPO NUMÉRICO
"""

num = 1_000_000
print(num)

# Errado do ponto de vista do float, mas gera uma tuple
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# Dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Converter um float para um int
    # Ao converter valores float para inteiros, se perde a precisão
res = int(valor) #convertendo o 'valor = 1.44'
print(res)
print(type(res))
