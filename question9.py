# Faça um programa que recebe a altura de um triangulo em um número inteiro e imprima-o utilizando asteriscos.


def triangulo(n):
	
	linhaP = 1 

	atualStar = 0
	linhaP = 1
	while(linhaP <= n ):
	
		if (atualStar < linhaP):
			print("* ", end = "")
			atualStar += 1
			continue
		
	
		if (atualStar == linhaP):
			print("")
			linhaP += 1
			atualStar = 0
		

triangulo(int(input('Insira um número: ')))





