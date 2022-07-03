# Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

timeOne = 'Flamengo'
timeTwo = 'Grêmio'
golOne = int(input('Primeiro numero: '))
golTwo  = int(input('Segundo numero : '))

if (golOne > golTwo):
    print( timeOne, 'ganhou por ', golOne, ' a ', golTwo, ' do ', timeTwo)
else:
    print( timeTwo, 'ganhou por ', golTwo, ' a ', golOne, ' do ', timeOne)
if (golOne == golTwo):
    print('A partida terminou em empate')



