# Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado deve ser #menor que a soma dos outros 2 lados.

n1 = 8
n2  = 9
n3 = 3


if (n2 + n3) > n1 and (n3 + n1) > n2 and (n1 + n2) > n3:
            print('As medidas dos lados formam um triângulo') 
else:
    print('As medidas dos lados não formam um triângulo')
    
