"""
Funções com parâmetros
- Funções que recebem dados para serem processados dentro da mesma;
 

#Retornando uma função
def quadrado(numero): #a função recebe o parâmetro 'numero' de entrada
    #return numero * numero
    return numero ** 3

print(quadrado(7))
print(quadrado(2))
print(quadrado(4))

#Assim também é válido:
ret = quadrado (5)
print(ret)

#print(quadrado()) #TypeError, ao tentar executar sem passa um parâmetro

------------------------

#Exemplo 2
def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Marcos')

------------------------


"""

#OBS: Funções podem ter n parâmetros de entrada, ou seja, podemos receber numa função
	#quantos parâmetros forem necessarios. Eles são separados por vígula.
#Exemplos:

def soma(a, b): #parâmetros
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(3, 5)) #argumentos
print(multiplica(10, 5))
print(outra(3, 2, 'geek '))


#OBS: Se for informado um numero errado de parâmetros ou argumentos, irá gerar TypeError











