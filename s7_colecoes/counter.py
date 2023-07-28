"""
Módulo Collections - Counter (Contador)

Collections > High performance Container Datetypes
	      Tipos de dados de container de alta performance

Counter > Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
	  que é parecido com um dicionário, contendo como chave o elemento da lista passada como
	  parâmetro e como valor a quantidade de ocorrências desse elemento.


#Realizando o import
from collections import Counter

#Exemplo 1
#Podemos utilizar qualquer iterável. Aqui utilizamos uma lista
lista = [1, 1, 1, 1, 4, 5, 5, 6, 44, 66, 64, 63, 64, 87, 33, 44, 33, 55, 67, 76]

#Utilizando o Counter
res = Counter(lista)

print(type(res)) #Tipo de objeto: Collections Counter
print(res) #Para cada elemento da lista, o Counter criou uma chave e colocou a quantidade de occorências.

#----

#Exemplo 2 - Imprimindo o Counter de uma string
print(Counter('Geek University'))


"""

#Realizando o import
from collections import Counter

#Exemplo 3 - 

texto = """ Luiz Carlos Alborghetti Alborghetti Alborghetti Alborghetti, mais conhecido apenas como Alborghetti foi um 
	   jornalista policial, radialista, apresentador de televisão e político brasileiro. 
		Por dezesseis anos, foi deputado estadual no Paraná """

palavras = texto.split() #split = cada uma das palavras como elemento de uma lista
#print(palavras)

res = Counter(palavras)
#print(res)

#Encontrando as cinco palavras com mais ocorrências no texto
print(res.most_common(5))
