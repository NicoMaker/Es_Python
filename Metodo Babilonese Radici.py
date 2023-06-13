print (" ")
print ("----------------------------------- METODO BABILONESE RADICI  ----------------------------------- ")
print("")


numero1 = input("INSERISCI UN NUMERO ---> ")  
numero1 = int (numero1)

epsilon = input("INSERISCI EPSILON (L'ERRORE) ---> ") 
epsilon = float (epsilon)  

passaggio = 0

X0 = pow(10, epsilon)
errore = abs(X0 ** 2 - numero1)

while errore >= epsilon:

    errore = abs(X0 ** 2 - numero1)
    X0 = 1/2 * (X0 + (numero1 / X0))
    passaggio += 1
else:
    print("")
    print(f"la radice approssimata di {numero1} è ---> {X0}")
    print(f"algoritmo fatto in ---> {passaggio} passaggi")
    print("")