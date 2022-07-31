#print range em ordem crescente
#for i in range(1,50):
        #   print(i)
           
#print range em ordem decrescente
#for i in range(50,0,-1):
           #print(i)
           
#print range em ordem decrescente e par apenas
#for i in range(50,0,-2):
          # print(i)
           
#print range em ordem decrescente e par apenas
def valores(inicial, final):
    if inicial <= final:
        for i in range(inicial, final+1):
           print(i)
    else:
        for i in range(inicial, final-1, -1):
            print(i)
            
valores(50,1)