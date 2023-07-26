"""
DICIONÁRIOS

#Em algumas linguagens de programação, os dicionários são conhecidos por mapas

Dicionários são coleções do tipo chave/valor.
Dicionários são representados por chaves {}
print(type({}))

OBS:
 - Chave e valor são separados por dois pontos 'chave:valor';
 - Tanto chave quanto valor podem ser de qualquer tipo de dado;
 - Podemos misturar tipos de dados;

----------------------

#Criação de dicionários
#Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

------------------------

"""

#Acessando elememtos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Forma 1 - via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
#print(paises['ru']) - caso seja feito acesso utilizando uma chave inexistente, haverá o erro KeyError

#Forma 2 - via get (RECOMENDADO)
print(paises.get('br'))
print(paises.get('ru'))









































