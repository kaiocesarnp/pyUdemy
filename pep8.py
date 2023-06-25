# Index of Python Enhancement Proposals / Índice de propostas de aprimoramento do Python
# São propostas de melhorias para a linguagem Python

# Poema The Zen of Python, comando = import this
# import this

# A ideia da PEP8 é que possamos escrever códigos Python de forma pythonica, ou seja, bonita. Segundo o The Zen of Python

# 1 - Utilize Camel Case para nomes de classes;
    # Ex: class Calculadora:
    #     class CalculadoraCientifica:

# 2 - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;
# def soma():
# def soma_dois():
# numero = 4
# numero_impar = 5

# 3 - Utilize 4(quatro) espaços para identação (Não use TAB)

# if 'a' in 'banana':
    # print('tem')
# ^^^4 espaços    

# 4 - Linhas em branco
# Separar funções e definições de classe com duas linhas em branco;
# Métodos dentro de uma classe devem ser separados com uma única linha em branco;
# class Classe:


# class Classe:

# 5 - Imports - Imports devem ser sempre feitos em linhas separadas
# Errado:
# import sys, os

# Certo:
# import sys
# import os

# Não há problemas em utilizar:
# from types import StringType, ListType
# Utilização de classes isoladas do pacote 'types'

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:
# from types import (
#     StringType,
#     ListType,
#     SetType,
#     OutroType
# )

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings
    # antes de constantes ou variáveis globais

# 6 - Espaços em expressões e instruções
# Não faça:
# funcao( algo[ 1 ], { outro: 2 } )

# faça:
# funcao(algo[1], {outro: 2})













