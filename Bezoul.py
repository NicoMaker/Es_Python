
print (" ")
print ("----------------------------------- BEZOUL  ----------------------------------- ")

numero1 = input("INSERISCI UN NUMERO: ") 
numero1 = int (numero1)                   
numero2 = input("INSERISCI UN NUMERO: ")  
numero2 = int (numero2)                    
print (" ")

a = numero1
b = numero2

quoziente = int (numero2 / numero1)
resto     = numero1 % numero2

while numero1 > numero2:
  
   while resto > 0:
    passaggio = passaggio + 1
    numero2 = resto
    resto = numero1 % numero2
    quoziente = int(numero1 / numero2)

else :

    