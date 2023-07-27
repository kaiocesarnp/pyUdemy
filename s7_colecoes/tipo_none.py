"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém, falar que é um tipo sem tipo é mais apropriado.

OBS:O tipo None é SEMPRE especificado com a primeira letra maiúscula
Certo: None
Errado: none

Quando utilizar?
- Quando se quer criar uma variável e inicializá-la com um tipo sem tipo, antes
de receber um valor final.

O tipo None em Py, é sempre considerado False
"""
numeros = None
print(numeros)
print(type(numeros))

numeros = 1.44, 2.33, 4.55
print(numeros)
print(type(numeros))
