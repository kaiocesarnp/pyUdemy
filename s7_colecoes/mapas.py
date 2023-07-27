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

"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}
print(receita)


























