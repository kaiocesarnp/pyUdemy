"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
  - Pode ou não receber entradas de dados e retornar uma saída de dados;
  - Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Caso escreva uma função que realize várias tarefas dentro dela, é bom fazer
	uma verificação para que a função seja simplificada.

- Várias funções já foram utilizadas neste curso:
print(), len(), max(), min(), count()...

#Exemplo de utilização de funções

cores = ['verde', 'amarelo', 'azul', 'branco'] #isso é uma lista

#Utilizando a função integrada (Built-in) do Python 'print()'
   #Toda função integrada, ou seja, que já vem na programação do Python é chamada de built-in
print(cores)
cores.append('roxo')
print(cores)

curso = 'Programação em Python: Essencial' #isso é uma string
print(curso)
#curso.append('Mais dados..') #AttributeError. A variável do tipo 'string' não tem o atributo 'append'
#print(curso)

-----------------

#Em Py, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:
nome_da_funcao > SEMPRE com letras minusculas e, se for nome composto, serapado por underline(snake case);
parametros_de_entrada > Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opicionais ou não;
bloco_da_funcao > Também chamado de corpo da função ou implementação, é onde o processamento da função acontece;
	Neste bloco, pode ter ou não retor da função.

OBS: Para definir uma função, utiliza-se a palavra 'def' informando ao Python que está se definindo uma função.
	Também é aberto o bloco de código com o já conhecido dois pontos : que é utilizado em Py para definir blocos.

-----------------

#Definindo a primeira função:

#Definição
def diz_oi():
    print('oi!')

#OBS: 	Veja que dentro da função, pode-se utilizar outras funções;
	#A função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer'oi';
	#Esta função não recebe nenhum parâmetro de entrada;
	#Esta função não retorna nada;

#Utilizando funções

#Chamada de execução
diz_oi()

#Nunca esqueça de utilizar o parênteses ao executar uma função:
#diz_oi - errado
#diz_oi () - errado, não espaço entre a função e o parênteses
#diz_oi() - certo

#Exemplo 2

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Viva o aniversariante!')

#Para multiplicar o resultado, ao invés de fazer isso:
cantar_parabens()
cantar_parabens()
cantar_parabens()

#Faça isso:
for n in range(4):
    cantar_parabens()

-----------------

"""
def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Viva o aniversariante!')

#Em Python, pode-se inclusive criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens
canta()
