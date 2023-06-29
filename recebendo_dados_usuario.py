"""
Recebendo dados do usuário
"""

# Entrada de dados
print("Qual seu nome? ")
nome = input().title()

# print('Seja bem-vindo(a) %s' % nome) # Exemplo de print 'antigo' 2.x

print('Seja bem-vindo(a) {0}'.format(nome)) # Exemplo de print 'moderno' 3.x

print("Qual sua idade? ")
idade = input()

# Saída de dados
# print("O(A) %s tem %s anos." % (nome, idade)) # Exemplo de print 'antigo' 2.x

print('A {0} tem {1} anos.'.format(nome, idade))# Exemplo de print 'moderno' 3.x
