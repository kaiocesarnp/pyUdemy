"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas;
Existem basicamente duas diferenças:
1- As tuplas são representadas por parênteses()
ex: print(type(()))

2- As tuplas são imutáveis, ou seja, ao se criar uma tupla, ela não muda. 
	Toda operação em um tupla gera uma nova tupla.

--------------------

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

---------------------------

#Desempacotamento com tupla
tupla = ('Geek University', 'Programação em Python: Essencial')
escola, curso = tupla 		#escola recebe 'geek..' e curso recebe 'programação...'
print(escola)
print(curso)

#OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar

#Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato de elas serem imutáveis.

---------------------------

#Soma*, valor máximo*, valor mínimo* e tamanho
# * Só se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

---------------------------

#Concatenação (juntar) de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) 
print(tupla1)
print(tupla2)

#tuplas são imutáveis, mas pode-se sobrescrever seus valores:
tupla1 = tupla1 + tupla2
print(tupla1)

---------------------------

#Verificar se determinado elemento está na tupla
tupla = (1, 2, 3)
print(2 in tupla)
print(22 in tupla)

---------------------------

#Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n) #para cada numero nesta tupla, imprima este número

#Indice
for indice, valor in enumerate(tupla):
    print(indice, valor)

---------------------------

#Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

---------------------------


#O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

#Iterar com while
i = 0
while i < len(meses): #Enquanto o i for menor que o tamanho (len) de meses
    print(meses[i])
    i = i + 1

#Verificar em qual indice o mes está na tupla.
#Se houver dois valores de mesmo nome, será impresso o primeiro da tupla
#OBS: Caso o elemento não exista, será gerado ValueError.
print(meses.index('Junho', 3)) #a partir do indice 3, no caso


"""

#Dicas na utilização de tuplas

#Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos numa coleção

#Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

#Slicing
#tupla[inicio:fim:passo]
print(meses[4:8])















