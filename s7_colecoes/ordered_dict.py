"""
Módulo Collections: Ordered Dict

#Em um dicionário, a ordem de inserção dos elementos não é garantida
#Já com o Ordered Dict, se tem a certeza de que os elementos serão ordenados

Ordered Dict > é um dicinario que garante a ordem de inserção dos elementos.

#Import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""

#Entendendo a diferença entre Dict e Ordered Dict

#Dicionários comuns - A ordem não importa - TRUE
dict1 = {'a': 1, 'b':2}
dict2 = {'b': 2, 'a':1}
print(dict1 == dict2)


#Ordered Dict - A ordem dos elementos importa - FALSE
from collections import OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})
print(odict1 == odict2)





























