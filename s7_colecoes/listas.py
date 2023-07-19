"""
Listas

Listas em Python funcionam como vetores/matrizer (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também podemos colocar QUALQUER tipo de dado.

Dinâmico: Não possui tamanho fixo, ou seja, pode-se criar a lista e simplesmente ir adicionando elementos;
Qualquer tipo de dado: Não possui tipo de dado fixo, ou seja, pode-se colocar qualquer tipo de dado;
As listas em Python são representadas por colchetes: []



"""
type([])

lista1 = [1, 99, 47, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#Pode-se facilmente checar se determinado valor está contido na lista
num = int(input('Qual o numero? '))
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

#-----------

lista5 = list('Geek University')
if 'e' in lista5:
    print('Encontrei a letra e')
else:
    print('Não encontrei a letra e')






