"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
  - Pode ou não receber entradas de dados e retornar uma saída de dados;
  - Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Caso escreva uma função que realize várias tarefas dentro dela, é bom fazer
	uma verificação para que a função seja simplificada.

- Várias funções já foram utilizadas neste curso:
print(), len(), max(), min(), count()...


"""

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

print(help(print))


















