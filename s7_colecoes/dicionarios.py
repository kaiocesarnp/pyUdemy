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

#Acessando elememtos
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

#Forma 1 - via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
#print(paises['ru']) - caso seja feito acesso utilizando uma chave inexistente, haverá o erro KeyError

#Forma 2 - via get (RECOMENDADA)
#Gera o valor 'None' ao invés de KeyError
print(paises.get('br'))
print(paises.get('ru')) #None

--
#Forma 2.1
pais = paises.get('br')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

--
#Forma 2.2
#Definindo um valor padrão ('não encontrado') para caso não haja a chave informada
pais = paises.get('ru', 'Não encontrado') #pega o valor da chave (br) e caso não encontre, coloque o valor 'não encontrado' no lugar.
print(f'Encontrei o país {pais}')

------------------------

#Verificar se determinada chave está dentro do dicionário
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises) #isso é valor, não chave, por isso da False

------------------------

#Podemos utilizar qualquer tipo de dado (in, float, string, boolean), inclusive lista,
	#tupla dicionário, como chaves de dicionarios.´'
#Tuplas são interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova Yor',
    (37.7749, 122.4194): 'Escritório em São Paulo'
}
print(localidades)
print(type(localidades))

------------------------

#Adicionar elementos num dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

#Forma 1 - Mais comum
receita['abr'] = 350
print(receita)

#Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})
print(receita)

-----

#Atualizando dados num dicionário
#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)

#CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados é a mesma.
#CONCLUSÃO 2: Em dicionários, NÃO pode haver chaves repetidas.

------------------------

#Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#Forma 1 - Mais comum
ret = receita.pop('mar') #pop remove o ultimo elemento da lista
print(ret)

print(receita)
#OBS 1: É necessário SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado
#OBS 2: Ao remover um objeto, o valor deste é sempre retornado - print(ret).

#Forma 2
del receita['fev']
print(receita)
#Se a chave não existir, será gerado um KeyError
#Neste caso, o valor removido não é retornado

------------------------

#Imagine que você tem um e-commerce, onde há um carrinho de compras com os seguintes produtos:
Carrinho de compras:
    Produto 1:
	- nome;
	- quantidade;
	- preço;
    Produto 2:
	- nome;
	- quantidade;
	- preço;

# 1 - Poderíamos utilizar uma lista para isso? Sim
carrinho = []

produto1 = ['Playstation 4', 1, 23000.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
#Teríamos que saber qual é o índice de cada informação no produto.

#----

# 2 - Poderíamos utilizar uma tupla para isso? Sim
produto1 = ('Playstation 4', 1, 23000.00)
produto2 = ('God of War', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
#Teríamos que saber qual é o índice de cada informação no produto.

#----

# 3 - Poderíamos utilizar um dicionário para isso? Sim
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

------------------------

#Métodos de dicionários:

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionário (zerar dados)
d.clear()
print(d)

#----
#Copiando um dicionário para outro

#Forma 1 - Deep copy
novo = d.copy() 
print(novo)

novo ['d'] = 4
print(d)
print(novo)

#----

#Forma 2 - Shallow Copy
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

"""
