"""
Loop while

Forma geral:
while expressão_booleana:
	//execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

exemplo 1:
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1 #se tirar essa linha, vira um loop infinito

#Obs: em um loop while é importante cuidar do critério de parada, para não causar um loop infinito. 
	#No caso do exemplo, o numero 10


"""

#exemplo 2:
resposta = ''
while resposta != 'sim'.upper():
    resposta = input('O Palmeiras tem mundial? ')
