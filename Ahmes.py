# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print (" ")
print ("----------------------------------- AHMES  ----------------------------------- ")

numero1 = input("INSERISCI UN NUMERO: ")  # dicharazione 1 numero
numero1 = int (numero1)                   # converto in int variabile numero1
numero2 = input("INSERISCI UN NUMERO: ")  # dicharazione 2 numero
numero2 = int (numero2)                    # converto in int variabile numero2
print (" ")

resto = 0                                 #variabie dove metto il restoo del passaggio
passaggio = 0                             # variabile dove conto i passaggi

print (" ")
print ("-------------------------------- SVOLGIMENTO -------------------------------- ")
print (" ")

while numero1 > 1:                 # mentre 1 numero maggiore di 1
    

    if numero1 %2 == 0:            # se pari
        
       passaggio = passaggio + 1                    # aumento passaggio
       print (f" {passaggio} passaggio : {numero1} è pari quindi ---> ({numero1} / 2) * (2 * {numero2})")   # stampa condizione
       numero1 = int (numero1 / 2  )                      # divido numero1 per 2
       numero2 = numero2 * 2                         # moltiplico numero 2 per 2
       
    elif numero1 %2 == 1:                          # altrimenti se è dispari
        
        passaggio = passaggio + 1                           # aumento passaggio
        print (f" {passaggio} passaggio : {numero1} è dispari quindi ---> ({numero1} - 1) * ({numero2} + {numero2})")   # stampa condizione
        numero1 = numero1 -1                                # tolgo a numero1 1
        resto = resto + numero2                             # vedo a cosa devo sommare numero2
       
        
else:                                                       #infine
    
    print(" ")
    print (" ALGORITMO FINITO")
    print("")
    print (f" Risultato Finale ---> {resto + numero2} ")                          # stampo risultato finale come somma tra resto e numero2
    print (f" Programma fatto in {passaggio} passaggi ")    # stampo passaggi fatti programma
    
    
        
        
        
        
        