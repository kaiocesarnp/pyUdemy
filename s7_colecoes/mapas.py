"""
Mapas - Conhecidos em Py como Dicionários
Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)

#Iterar sobre dicionários
for chave in receita: #pra cada chave dentro de receita, imprima a chave
    print(chave)

for chave in receita:
    print(receita[chave]) #pra cada chave dentro de receita, imprima o valor da receita

#---

#Melhorando o código, gerando chave e valor juntos
for chave in receita:
    print(f'Em {chave} recebi R${receita[chave]}')

#Acessando as chaves
print (receita.keys())

#Utilizando o keys para fazer o for - Método recomendado do Python
for chave in receita.keys():
    print(receita[chave])

#Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#Desempacotamento de dicionários
print(receita.items()) #gera uma lista contendo tuplas das chaves e valores

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

#Soma*, valor max*, valor min*, tamanho
#só se os valores forem todos inteiros ou reais
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""
