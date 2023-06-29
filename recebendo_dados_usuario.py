"""
Recebendo dados do usuário
"""

# Entrada de dados
print("Qual seu nome? ")
nome = input().title()

print('Seja bem-vindo(a) %s' % nome)

print("Qual sua idade? ")
idade = input()

# Saída de dados
print("O(A) %s tem %s anos." % (nome, idade))