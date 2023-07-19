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


"""
#Podemos checar se determinado valor está contido na lista
num = int(input('Qual o numero? '))
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

letra = input('Qual o a letra?')
if letra in lista5:
    print(f'Encontrei a letra {letra}')
else:
    print(f'Não encontrei a letra {letra}')

#--------------

#Podemos ordenar uma lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

#--------------

#Podemos contar o numero de ocorrência de um valor numa lista
print(lista1.count(1))
print(lista5.count('e'))

#--------------

#Adicionar elementos em listas:
    #Utilizamos a função 'append' e 'extend'
    #Com append, só é possivel adicionar um elemento por vez

print(lista1)
lista1.append(35)
print(lista1)

#Adicionando mais elementos, no formato de nova lista dentro da lista:
lista1.append([8, 3, 1])
print(lista1)
if [99, 39, 19] in lista1:
    print('Found list')
else:
    print('List not found')

#A função 'extend' faz o mesmo que a 'append'. Mas ao adicionar, os elementos não formam uma nova lista dentro da primeira lista
    #Os elementos são adicionados diretamente na lista
    #O 'extend' não aceita valor único
lista1.extend([133, 253, 643])
print(lista1)

#--------------

"""


