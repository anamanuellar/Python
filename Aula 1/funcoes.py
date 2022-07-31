def Soma (valorA, valorB):
  return valorA + valorB
  
def Media(x, y):  
    return (x + y)/2
 
    
def parImpar(valor:int):
  if (valor % 2 == 0):
    return "Esse número é par"
  else:
    return "Esse número é ímpar"

def Soma (nome = str()):
  return nome
print(Soma(3))

# Cria uma função que valida idade de 50 a 150 anos, inclusive retornar True se válido

def validarIdade(idade):
  if 5 <=idade<=150:
    return True
  else:
    return False
  
#----------------
def validarIdades(idade):
      
    return True if (5 <=idade>=150) else False