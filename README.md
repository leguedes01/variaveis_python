## variaveis_python                                      
                                                            
age =int( input('Qual sua idade: ') )                 

if age >= 18 and age <= 65:                              
                                                      
     print('Você já está na idade de votar')             
                                                      
else:                                                   
                                                      
     print("Você não pode votar")                        

________________________________________________________________________________________________________________________________________
### programa em python com separoções, com números inteiros, negativos e positivos.

numero1 = 1
numero2 = -8
numero3 = +10 

age =int( input('dgite um numero: ') )
if (numero1 == 1):
    print("numero inteiro")
else :
    ("tente novamente")
if (numero2 == -8):
    print("numero negativo")
else :
    ("tente novamente")
if (numero3 == +10):
    print("numero positivo")
else :
    ("tente novamente")
    _____________________________________________________________________________________________________________________________________

  #### programa python selecionaddo cada triangulo corretamente.

  age =int( input('dgite um numero: ') )
if age >= 8 and age <= 13:
    print("é o trinagulo isosceles")
if age >= 5 and  age <= 9:
    print("é o trinagulo escaleno")
if age >= 10 and  age <= 12:
    print("é o trinagulo equilatero")    
________________________________________________________________________________________________________________________________________
##### lists
list = [1,3,6,9,5]
print(list)

lista.remove(1)
del lista[0]
print(lista)
____________________________________________________________________________________________________________
from datetime import datetime, timedelta

today = datetime.now() 
        print("hoje", today)
   yesterday = today - timedelta(days=1)
        print("ontem", yesterday)
   tomorrow = today + timedelta(days=1)
        print("amanhã", tomorrow )
   time_difference = tomorrow - yesterday
        print(time_difference)





    
