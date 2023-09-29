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



> from datetime import datetime, timedelta
>>>
KeyboardInterrupt
>>>  from datetime import datetime, timedelta
  File "<stdin>", line 1
    from datetime import datetime, timedelta
IndentationError: unexpected indent
>>> from datetime import datetime, timedelta
>>> today = datetime.now()
>>> print("hoje" , today)
hoje 2023-09-27 20:22:07.713184
>>> yesterday = today - timedelta(days = 1)
>>> print("ontem", yesterday)
ontem 2023-09-26 20:22:07.713184
>>> tomorrow = today + timedelta(days = 1)
>>> print("amanhã" , tomorrow)
amanhã 2023-09-28 20:22:07.713184
>>> time_difference = tomorrow - yesterday
>>> print("alguns dias" , time_difference)
alguns dias 2 days, 0:00:00
>>>

__________________________________________________________________________________________________
# EXERCÍCIO 01

class Dog:
   def __init__(self, raca, peso, sexo):
       self.raca = raca
       self.peso = peso
       self.sexo = sexo
       
       dog = dog("Golden" , "190peso" , "Macho")
       
print("A raça do cachorro é", Dog.raca)
print("O peço do cachorro é", Dog.peso)
print("O sexo do cachorro é", Dog.sexo)
       
       
       # EXERCÍCIO 02
       
class Retangulo:
    def __init__(self, H, L, C):
            self.H = altura
            self.L = largura
            self.C = cumprimento
            
    Retangulo = Retangulo(10 , 20 , 18)
    
    
    print("A altura do retangulo é" Retangulo.H)
    print("O cumprimento do retangulo é" Retangulo.C) 
    return 
