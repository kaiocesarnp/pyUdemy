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

"""

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


























