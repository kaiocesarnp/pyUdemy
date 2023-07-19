"""
Estruturas lógica: and(e), or(ou), not(não), is(é)

Operadores unários:
	not

Operadores binários:
	and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True.
Para o 'or', um ou outro valor precisa ser True.
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False. Se for False vira True.
Para o 'is', o valor é comparado com um segundo.
"""

ativo = False
logado = True

#and
if ativo and logado:
    print('Usuário ativo no sistema.')
else:
    print('Ative sua conta. Por favor, cheque seu e-mail.')

#or
if ativo or logado:
    print('Usuário ativo no sistema.')
else:
    print('Ative sua conta. Por favor, cheque seu e-mail.')

#not
#se não estiver ativo, faz isso:
if not ativo:  
    print('Ative sua conta. Por favor, cheque seu e-mail.')
else:
    print('Bem-vindo usuário.')
print(not True)

#is
print(ativo is False)
