1
print ("--------ALGORITMO DI EUCLIDE --------------------")
print (" ")

divisore = int (input("INSERISCI IL 1 NUMERO : "))
dividendo = int (input("INSERISCI IL 2 NUMERO : "))

a = divisore 
b = dividendo  

resto = 1


print (" ")
print ("--------SVOLGIMENTO --------------------")
print (" ")

while (resto != 0):
    
    restoprima = resto
    resto = dividendo % divisore
    dividendo = divisore
    divisore = resto

else: 

    print (f"il MCD di {a} , {b} = {dividendo }")
    print (" ")