"""
Recebendo dados do usuário
"""

# Entrada de dados
print("Qual seu nome? ")
nome = input().title()

# print('Seja bem-vindo(a) %s' % nome) # Exemplo de print 'antigo' 2.x

# print('Seja bem-vindo(a) {0}'.format(nome)) # Exemplo de print 'moderno' 3.x

print(f'Seja bem-vindo(a) {nome}') # Exemplo de print 'mais atual' 3.7x

print("Qual sua idade? ")
idade = input()

# Saída de dados
# print("O(A) %s tem %s anos." % (nome, idade)) # Exemplo de print 'antigo' 2.x

# print('O(A) {0} tem {1} anos.'.format(nome, idade))# Exemplo de print 'moderno' 3.x

print(f'O(A) {nome} tem {idade} anos.') # Exemplo de print 'mais atual' 3.7x

# int(idade) => cast
# Cast é a 'conversão' de um tipo de dado para outro
print(f'O(A) {nome} nasceu em {2023 - int(idade)}')

