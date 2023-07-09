"""
Dois casos de escopo:

1 - Variáveis globais:
    - São reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis locais:
    São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
        está limitado ao bloco onde foi declarada
    
Para declararmos variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinamica. Isso significa que ao declararmos uma
variável, nós não colocamos o tupo de dado dela.
Este tipo é inferido ao atribuirnos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""


""""
# Exemplo de variável global:
numero = 42
print(numero)
print(type(numero))
"""

# Exemplo de variável local:
    # o print da variavel 'novo' não é impresso fora do if pois ela é uma variável local.
        # Neste caso apenas sendo um número menor que o do if > 10
numero = 2

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)