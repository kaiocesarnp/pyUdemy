"""
Funções com parâmetro padrão (default Paramters)

- Funções onde a passagem de parâmetros seja opcional;

------
Porque utilizar parâmetros com valor default?
- Nos permite ser mais flexíveis nas funções
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

------
Quais tipos de dados podemos utilizar como valores default para parâmetros:
- Qualquer tipo: números, strings, floats, booleanos, listas, tuplas, dicionários, funções etc.

#Exemplo de função onde a passagem de parâmetro é opcional:
print('Geek University')
print()

#Exemplo de função onde a passagem de parâmetro é obrigatória:
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
#print(quadrado()) #TypeError

-----------------------

def exponencial (numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))


--------------------

#Ao se definir uma função, caso não seja passado parâmetros, dará TypeError
	#Caso seja passado, o TypeError não será impresso
def soma(num1=5, num2=7): #parâmetros: 5, 4
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma()) #TypeError


--------------------

#Exemplo mais complexo
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor: 	#instrutor True
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


---------------------

#Funções como parâmetro
def soma(num1, num2): #parametros obrigatórios
    return num1 + num2

def mat(num1, num2, fun=soma): #2 parâmetros obrigatórios e 1 opcional(fun, que está inicializado com 'soma' que é a função inicial)
    return fun(num1, num2)		#ou seja, se o usuário informar outra função ela será utilizada nesta linha aqui, caso não, fica a padrão 'soma'

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

----------------------


"""












