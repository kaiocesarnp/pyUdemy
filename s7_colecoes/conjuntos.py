"""
Conjuntos 

- Conjuntos em qualquer linguagem de programação faz referência à Teoria dos Conjuntos da Matemática.
- Em Py, os conjuntos são chamados de Sets;

Dito isso, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são úteis quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. 
    Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (sets) e mapas (dicionarios) em Py:
   - Um dicionário tem chave/valor;
   - Um conjunto tem apenas valor;

#----------------
#Definindo um conjunto:

#Forma 1
#Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será 
   #ignorado sem gerar error e não fará parte do conjunto.
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #Repare que há valores repetidos
print(s)
print(type(s))

#Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#Verificar se determinado elemento está contido no conjunto
n = int(input("Digite um número para verificar se está no conjunto: "))
if n in s:
    print(f"Tem o {n} no conjunto.")
else:
    print(f"Não tem o {n} no conjunto.")

#--------------------------

#Importante lembrar que, além de não haver valores duplicados, não há ordem

#listas aceitam valores duplicados, então há 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

#tuplas aceitam valores duplicados, então há 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

#dicionarios não aceitam chaves duplicadas, então há 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

#conjuntos não aceitam valores duplicados, então há 8 elementos
#em conjuntos não há ordem!
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

#---------------------

#Assim como todo outro conjunto em Py, podemos colocar tipos de dados misturados em Sets
s= {1, 'b', True, 42.22, 22}
print(s)
print(type(s))

#Podemos iterar num set normalmente
for valor in s:
    print(valor)

#--------------------

#Usos interessantes com sets
#Imagine que foi feito um formulário de cadastro de visitantes numa feira ou museu,
    #e os visitantes informam manualmente a cidade de onde vieram
#Pode-se adicionar cada cidade numa lista Py, já que numa lista pode-se adicionar
    #novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']
print(cidades)
print(len(cidades)) #quantas pessoas foram?

#Quantas cidades distintas, ou seja, únicas, há?
print(len(set(cidades)))

#--------------------

#Adicionando elementos num conjunto
s = {1, 2, 3}

s.add(4)
s.add(4) #duplicidade não gera erro, apenas é ignorado e não é adicionado
print(s)

#--------------------

#Removendo elementos num conjunto
s = {1, 2, 3}
print(s)

#Forma 1
#Caso o valor não seja encontrado, será gerado o erro KeyError. Nenhum valor é retornado
s.remove(3) #Não é indice. Informamos o valor a ser removido.
print(s)

#Forma 2
#Se o valor não for encontrado, nenhum erro é gerado
s.discard(2)
print(s)

#----------------------

#Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

#Forma 1 - Deep Copy
novo = s.copy()
print(novo)
novo.add(4)
print(novo)
print(s)

#Forma 2 - Shallow Copy
novo = s
novo.add(4)
print(novo)
print(s)

#----------------------

#Removendo todos os itens de um conjunto
s = {1, 2, 3}
print(s)

s.clear()
print(s)

#----------------------

#Métodos matemáticos de conjuntos

#Imagine dois conjuntos de estudantes: Python e Java
#Alguns alunos que estudam py também estudam java

estud_python = {'Marcos', 'Patricia', 'Elen', 'Pedro', 'Julia', 'Guilherme'}
estud_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

#Gerar um conjunto com nomes de estudantes únicos

#Forma 1 - Utilizando union
unicos1 = estud_python.union(estud_java)
print(unicos1)

#Forma 2 - Utilizando o caractere pipe |
unicos2 = estud_python | estud_java
print(unicos2)

#------

#Gerar um conjunto de estudantes que estão em ambos os cursos

#Forma 1 - Utilizando intersection
ambos1 = estud_python.intersection(estud_java)
print(ambos1)

#Forma2 - Utilizando o &
ambos2 = estud_python & estud_java
print(ambos2)

#------

#Gerar um conjunto de estudantes que não estão no outro curso
so_python = estud_python.difference(estud_java)
print(so_python)

so_java = estud_java.difference(estud_python)
print(so_java)

#-----------------

#Soma*, valor max*, valor min*, tamanho
#Só se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))


"""
