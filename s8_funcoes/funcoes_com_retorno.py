"""
Funções com Retorno

OBS: Em Py, quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra
	reservada 'return'.
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função.
	Podemos passar a execução da função para outras funções.

#Exemplo de função que não retorna nada
def quadrado_de_7():
    print(7 * 7)

ret = quadrado_de_7() #Não retorna nada
print(f'Retorno {ret}')

-------------------

#Exemplo de função que retorna valor
#Reescrevendo o código acima
def quadrado_de_7():
    return 7 * 7

#Cria-se uma variável para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

#Outra forma, mais simples de retornar:
print(f'Retorno: {quadrado_de_7()}')

-----------------
#Mais exemplo:
def diz_oi():
    return 'OI '

alguem = 'Pedro!'
print(diz_oi() + alguem)

------------------

OBS: Sobre a palavra reservada 'return'
	1 - Ela finaliza a função, ou seja, ela sai da execução da função;
	2 - Podemos ter em uma função, diferentes returns;
	3 - Podemos em uma função, retornar qualquer tipo de dados e até mesmo múltiplos valores;

#Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado antes o retorno...')
    return 'Oi!' #A função é finalizada aqui, por isso o print debaixo não é executado
    print('Estou sendo executado após o retorno...')

print(diz_oi())

------------------
#Exemplo 2 - Podemos ter em uma função, diferentes returns;
def nova_funcao():
    variavel = True
    if variavel :
	 return 4 #se a variavel for true, retorna 4
    elif variavel in None:
	 return 3.2 #se não retorna 3.2
    return'b'

print(nova_funcao())
-
----------------

#Exemplo 3
#Numa função, 
def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao
print(num1, num2, num3, num4)

----------------

#Criando função para jogar a moeda
from random import random

def joga_moeda():
    #Gera um numero pseu-randômico (é aleatória mas gera repetição) entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara' #se o valor for maior que 0.5 retorna 'cara
    return 'Coroa'    #se não for (else) retorna 'coroa'

print(joga_moeda())

---

#Exemplo com jokenpo
from random import random

def jokenpo():
    if random() < 0.3:
        return 'Pedra' 
    elif 0.3 < random() < 0.6:
        return 'Papel'  
    elif random() > 0.6:
        return 'Tesoura'
    else:
        return 'Invalid'  # Retorno padrão caso nenhuma das condições anteriores seja atendida

print(jokenpo())


"""
