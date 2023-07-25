"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas;
Existem basicamente duas diferenças:
1- As tuplas são representadas por parênteses()
ex: print(type(()))

2- As tuplas são imutáveis, ou seja, ao se criar uma tupla, ela não muda. 
	Toda operação em um tupla gera uma nova tupla.

#CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

#'representadas' significa que ao serem impressas(print), as tuplas aparecerão com ()
	#Mas o exemplo 2 (tupla2) também está certo.

#CUIDADO 2: Tuplas com um elemento
tupla3 = (4) #isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) #isso é uma tupla
print(tupla4)
print(type(tupla4))

#CONCLUSÃO: tuplas são definidas pelo uso da vírgula e, não dos parênteses
(4) - não é tupla
(4, ) - é tupla
4, - é tupla

---------------------------

#Gerando tupla com range (inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

"""
#Desempacotamento com tupla

tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla
print(escola)
print(curso)

18:17






























