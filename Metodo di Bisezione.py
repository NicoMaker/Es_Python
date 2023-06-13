print(" ")
print("----------------------------------------------- METODO DI BISEZIONE ----------------------------------------------")
print("")
print("----------------------------------- METODO TROVARE GLI ZERI DI UNA FUNZIONE  ----------------------------------- ")
print("")


numero1 = input("INSERISCI UN NUMERO ---> ")
numero1 = int(numero1)

numero_min = -10
numero_max = 10
passaggio = 0

x = (numero_max + numero_min) / 2
y = (x - 1) * (x - 2) * (x + 1)

print("")
while y != 0 :

    if x > 0 : 

        passaggio = passaggio + 1
        print(f"IL valore nel {passaggio} passaggio è ---> {x}")
        x = (x + numero_min) / 2 
        numero_min = (x + numero_min) / 2 

    elif x < 0 :
        
        passaggio = passaggio + 1
        print(f"IL valore nel {passaggio} passaggio è ---> {x}")
        x = (x + numero_max) / 2 
        numero_max = (x + numero_max) / 2 

    elif x == 0 :

        passaggio = passaggio + 1
        print(f"IL valore nel {passaggio} passaggio è ---> {x}")
        x = (x + numero_min) / 2 
        numero_min = (x + numero_min) / 2 

    y = (x-1) * (x-2) * (x+1)

else: 
    print("")
    print(f"IL VALORE E' ---> {x}")
    print(f"ALGORITMO FATTO IN ----> {passaggio} PASSAGGI")