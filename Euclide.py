# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:10:00 2022

@author: Utente
"""

print (" ")
print ("----------------------------------- EUCLIDE  ----------------------------------- ")

numero1 = input ("INSERISCI IL NUMERO IL QUALE VOGLIO FARE LA DIVISIONE: ")   #inserisci numero1
numero1 = int (numero1)                                                       #convertire in intero numero1
numero2 = input ("INSERISCI IL NUMERO PER IL QUALE VOGLIO DIVIDERE: ")        # inserisci numero2
numero2 = int (numero2)                                                       #convertire in intero numero2

passaggio = 0
resto = numero1 % numero2          # resto tra numero1 e numero2
quoziente = int (numero1/numero2)  # quoziente tra numero1 e numero2

print("")
print ("-------------------------------- SVOLGIMENTO ----------------------------------- ")
print("")

while resto > 0:
    passaggio = passaggio + 1
    print (f" {passaggio} passaggio ----> {numero1} = {numero2} * {quoziente} + {resto}")
    numero1 = numero2
    numero2 = resto
    resto = numero1 % numero2
    quoziente = int(numero1 / numero2)
    
    
else:
    print(" ")
    print (" ALGORITMO FINITO")
    print(" ")
    print (f" Programma fatto in {passaggio} passaggi ")    # stampo passaggi fatti programma
    print (f"MCD -----> {numero2}")


