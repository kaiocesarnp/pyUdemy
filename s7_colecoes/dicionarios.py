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


"""

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

#Atualizando dados num dicionário
#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 600})
print(receita)



























