"""
Precisamos conhecer o loop for para usar os ranges.
Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, não de forma aleatoria, 
mas sim de maneira especificada.

Formas gerais:

exemplo 1:
range(valor_de_parada)
obs: valor_de_parada não incluído (inicio padrao 0 e passo de 1 em 1)

for num in range(11):
    print(num)

exemplo 2:
range(valor_de_inicio, valor_de_parada)
obs: valor_de_parada não incluído (inicio espicificado e passo de 1 em 1)

for num in range(3, 11):
    print(num)

exemplo 3:
range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada não incluído (inicio espicificado e passo espicificado)

for num in range(5, 50, 5):
    print(num)

exemplo 4 (é igual a 3 só que inversa)
range(valor_de_inicio, valor_de_parada, passo)
obs: valor_de_parada não incluído (valor_de_inicio espicificado e passo espicificado)


"""

for num in range(10, -1, -1):
    print(num)



















