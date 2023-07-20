"""
Listas

Listas em Python funcionam como vetores/matrizer (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também podemos colocar QUALQUER tipo de dado.

Dinâmico: Não possui tamanho fixo, ou seja, pode-se criar a lista e simplesmente ir adicionando elementos;
Qualquer tipo de dado: Não possui tipo de dado fixo, ou seja, pode-se colocar qualquer tipo de dado;
As listas em Python são representadas por colchetes: []
"""

"""
type([])
lista1 = [1, 99, 47, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345] #lista com diversos tipos de dados


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

#Inserir novo elemento na lista informando a posição do índice
    #Isso não substitui o valor inicial, o mesmo será deslocado para o próximo índice
lista1.insert(2, 'novo valor')
print(lista1)

#--------------

#Juntando duas listas
lista1 = lista1 + lista2
print(lista1)

#Outra forma de juntar listas:
lista1.extend([lista2, lista5])
print(lista1)

#--------------

#Inverter listas, utilizando 'reverse'
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

#Outra forma
print(lista1[::-1])
print(lista2[::-1])

#--------------

#Copiar uma lista
lista6 = lista2.copy()
print(lista6)

#--------------

#Tamanho da lista (quantos elementos têm)
print(len(lista2))

#--------------

#Remover o último elemento de uma lista
    #O pop não somente remove o último elemento, como também o retorna
print(lista5)  #Antes de remover
lista5.pop()
print(lista5)  #Depois de remover

#Remover um elemento pelo índice
    #Os elementos à direita deste índice, serão deslocados para a esquerda
    #Se não houver elemento no índice informado, haverá o erro IndexError
lista5.pop(2)
print(lista5)

#--------------

#Remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

#--------------

#Repetir elementos numa lista
nova = [1, 2, 3]
print(nova)

nova = nova * 3
print(nova)

#--------------

#Converter uma string numa lista
    #Por padrão, o 'split' separa os elementos da lista pelo espaçõ entre elas
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#Outra forma
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') #indica que o separador é a vírgula, não mais o espaço
print(curso)

#--------------

#Convertendo uma lista em string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

#curso = ' '.join(lista6) #Adiciona espaço entre os elementos e tranforma em string
curso = '$'.join(lista6) #Adiciona cifrão entre os elementos e tranforma em string
print(curso)

#--------------

#Iterando sobre listas

#Utilizando 'for'
soma = 0
for elemento in lista4:
    print(elemento)
    soma = soma + elemento
print(soma)

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

#Utilizando while
carrinho = [] #cria uma lista vazia
produto = ''  #cria uma variavel do tipo string

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

	#quando o usuário digitar sair, sai do loop while e vai para o loop for
for produto in carrinho:
    print(produto)

#--------------

#Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

#--------------

#Fazer acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores)

#Fazer acesso aos elementos de forma indexada inversa
    #Para entender melhor o índice negativo, pense num círculo, onde o final de um
	#elemento está ligado ao início da lista
print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-5]) #erro

for cor in cores:
   print(cor)

#enquanto o indice for menor que o len(tamanho, 4) das cores, imprima cores na posição indice
indice = 0
while indice < len(cores):
    print(cores[indice]) 
    indice = indice + 1

#Gerar indice num for
for indice, cor in enumerate(cores):
    print(indice, cor)

cores = list(enumerate(cores))
print(cores)

#--------------

#Listas aceitam valores repetidos
lista = []
lista.append(38)
lista.append(33)
lista.append(38)
lista.append(33)

print(lista)


#--------------
numeros = [5, 6, 7, 5, 8, 9, 10]

#Outros métodos não tão importantes mas também úteis:
#Econtrar o índice de um elemento na lista
    #Retorna o índice do primeiro elemento encontrado
    #Caso não tenha o elemento na lista, será apresentado erro ValueError
	#Em qual índice está o valor 6?
print(numeros.index(6))
	#Em qual índice está o valor 9?
print(numeros.index(9))


#Fazer busca dentro de um range, ou seja, qual índice começar a buscar
	#buscando o índice do valor 5 a partir do índice 1, sem contar com índice 0
print (numeros.index(5, 1))

#buscando dentro de um range, informando início/fim
	#buscar o indice do valor 8, enre os índice 3 e 6
print(numeros.index(8, 3, 6)) 

#--------------

#Revisão de slicing
    #lista(inicio:fim:passo)

#Trabalhando com slice de lista com o parametro 'inicio'
lista = [1, 2, 3, 4]

print(lista[::]) #pegando todos os elementos
print(lista[1:]) #iniciando no índice 1 e pegando todos os elementos restantes

#Trabalhando com slice de lista com o parametro 'fim'
print(lista[:2]) #começa em 0 e pega até o índice 2 -1, porque o  indice 2 não está incluso
print(lista[:4]) #começa em 0 e pega até o índice 4 -1
print(lista[1:3]) #começa em 1 e pega até o índice 3 -1
print(lista[1:-1])

#trabalhando com slice de lista com o parametro 'passo'
print(lista[1::2]) #começa em 1, vai até o final, de 2 em 2
print(lista[::2]) #começa em 0, vai até o final, de 2 em 2
print(lista[1::-1]) #começa em 1, vai até o final, de -1 em -1

#---------------

#Invertendo valores numa lista
nomes = ['Geek', 'University']
nomes[0], nomes [1] = nomes [1], nomes[0] #zero vira um e um vira zero
print(nomes)

#outra forma
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

#--------------

#soma*, valor máximo*, valor mínimo*, tamanho
	# * se os valores forem todos inteiros ou reais
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #tamanho da lista

#--------------

#Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

#--------------

#Desempacotamento de listas
	#caso haja mais elementos para desempacotar do que variáveis 
	    #para receber os valores, dará ValueErro. O mesmo vale para o contrário
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

#--------------

#Copiando uma lista para outra (deep copy e shallow copy)
    #forma 1 - Deep Copy
	#ao utilizar 'lista.copy()', copia-se os dados de uma para outra, mas elas são independentes, ou seja,
	    #modificando a lista, a original não é afetada. Isso em Python é chamado de Deep Copy (ou cópia profunda)
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(nova)


    #forma 2 - Shallow Copy
	#cópia via atribuição. Após modificar uma das listas, a original também é modificada.
	    #Isso em python é chamado de shallow copy
lista = [1, 2, 3]
print(lista)

nova = lista
nova.append(4)
print(lista)
print(nova)

#--------------

"""
