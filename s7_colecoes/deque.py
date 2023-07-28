"""
Módulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance

"""

#Import
from collections import deque

#Criando deques
deq = deque('geek')
print(deq)

#Adicionando elementos no deque
deq.append('y') #adiciona no final
print(deq)

deq.appendleft('k') #adiciona no começo
print(deq)

#Remover elementos
print(deq.pop()) #remove e retorna o último elemento
print(deq)

print(deq.popleft()) #remove e retorna o primeiro elemento
print(deq)
