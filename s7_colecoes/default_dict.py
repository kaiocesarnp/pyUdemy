"""
Módulo Collections - Defeaut Dict

Defaut Dict > Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo
		utilizar um lambda para isso. Este valor será utilizado sempre que não
		houver um valor definido. 
		Caso tente acessar um chave que não exista, esta chave será criada e, o 
		valor será atriubuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.


"""

#Import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

print(dicionario['outro']) #Se fosse num dicionario comum, ao passar um parâmetro inexistente ('outro') no comando inicial, geraria KeyError. Mas neste caso, não.
print(dicionario)













