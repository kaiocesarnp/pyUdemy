"""
Loop for

Loop > Estrutura de repetição
For > Uma dessas estruturas

Utiliza-se Loops paraa iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
-String
   nome = 'Geek University'
-Lista
   lista = [1, 3, 5, 7, 9]
- Range
   numeros = range(1, 10)

"""

"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar numa lista

#Exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)

#Imprimindo o nome em sequencia, sem ser uma letra embaixo da outra:
for letra in nome:
    print(letra, end='')

#Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

#Exemplo de for 3 (iterando sobre um range)
#Obs: O valor final não é incluío
for numero in range(1, 10):
    print(numero)


#Qual é o indice?
#O 'enumerate' gera para cada sequência do iterável, um índice
#((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')...)
for indice, letra in enumerate(nome):
    print(nome[indice])

#Outro método:
for indice, letra in enumerate(nome):
    print(letra)

#Outro método:
#Obs: Quando há um valor que pode ser descartado, utiliza-se o underline.
for _, letra in enumerate(nome):
    print(letra)

#Printando indice e valor
for valor in enumerate(nome):
    print(valor[0]) #somente o indice, numeros
    print(valor[1]) #somente a letra


#-------------

#Utilização do for noutros casos:

qtd = int(input('Quantas vezes esse loop deve rodar?')) #lembre-se que o último número não é incluso
for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')


#Imprimindo emojis:
#original: U+1F60D - U+1F605
#modificado: U00001F60D - U0001F605

for num in range(1, 11):
    print('\U00001F60D' * num)

"""
#Outra forma:
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F605' * num)




