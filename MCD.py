# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:04:43 2022

@author: Utente
"""

number1 = input("Inserisci un numero: ")
number1 = int(number1)
number2 = input("Inserisci un altro numero: ")
number2 = int(number2)
quoziente = int(number1 / number2)
resto = number1 % number2
# Serve per Bezout
lista = [number1, number2, quoziente, resto]
passaggi = 1.
print(f"{number1} = {number2} * {quoziente} + {resto}\n")
if number1 % number2 == 1:
    print(f"I numeri di Bezout sono: 1 e -{int(number1/number2)}")
else:
    # algoritmo di euclide
    while resto > 1:
        number1 = number2
        number2 = resto
        quoziente = int(number1 / number2)
        resto = number1 % number2
        lista2 = [number1, number2, quoziente, resto]
        print(f"{number1} = {number2} * {quoziente} + {resto}\n")
        # l'idea è di convertire i passaggi precedenti in un quadrato
        for i in lista:
            lista2.append(i)
        # la lista diverrà sempre più grande, inglobando TUTTI i valori
        lista = lista2
        # serve per Bezout
        passaggi += 1
    else:
        print(f"Il risultato è stato raggiunto in {passaggi} passaggi")
        if resto == 1:  # Nel caso  MCD != 1, allora è il resto
            print(f"Il massimo comune divisore è: {resto}\n")
        else:  # se MCD > 1,allora MCD = number2
            print(f"Il masimo comune divisore è: {number2}\n")

    if passaggi > 1:
        print(lista)
        sost = 4
        # Causa di ore perse a fare il procedimento di Bezout
        # print(f"{lista2[3]} = {lista2[0]} + {lista2[3-2]} * ( {(-1)*lista2[3-1]} )")
        # print(f"{lista2[3]} = ( {lista2[sost]} * (1) + {lista2[sost+1]} * -{lista2[sost+2]} ) * ( -{lista2[2]} ) +  {lista2[sost]} * ({lista2[2]})")
        # print(f"{lista2[3]} ={lista2[sost]} * ({-lista2[2]}) + {lista2[sost+1]} * ({-lista2[sost+2] * (-lista2[2])}) + {lista2[sost-4]} * ({lista2[2]})")
        # Ciò che contano sono i primi valori di x e y, il resto viene per somme e mltipliche di specifici numeri nella lista2
        print(f"{lista2[3]} = {lista2[sost]} * ({-lista2[2]}) + {lista2[sost-4]} * ( {lista2[2] + lista2[sost+2]} )")
        x = -lista2[2]
        y = lista2[2] + lista2[sost+2]
        print(f"x è: {x}, mentre y è: {y}")
        # Tiene tracci a dei numeri nel blocchi di procedimento durante l'algoritmo di Euclide
        incr = 0
        while passaggi >= 3:
            print("---------------------------Bezout------------------------------")
            # serve lista[2] per moltiplicare i numeri in successione
            if x < 0 and lista2[10+incr] == 1:
                print(f"x<0 and lista2[{10+incr}]==1")
                print(
                    f"I numeri di Bezout sono: {y} e {(-y*lista2[10+incr])+x}")
                print(x)
                print(y)
                y = -y+x
                x = x-y
            elif x < 0:
                # Quando Lista[10+incr] != 0, devo dividere il nuovo valore di x per lista2[10+incr]
                print("x<0")
                print(f"I numeri di Bezout sono: {y} e {(-y*lista2[10+incr])+x}")
                print(x)
                print(y)
                y = (-y*lista2[10+incr])+x
                x = int((-y+x)/lista2[10+incr])
            elif y < 0 and lista2[10+incr] == 1:
                print(f"y<0 and lista2[{10+incr}]==1")
                print(
                    f"I numeri di Bezout sono: {y} e {(-y*lista2[10+incr])+x}")
                print(x)
                print(y)
                y = -y+x
                x = x-y
            elif y < 0:
                print("y<0")
                print(f"I numeri di Bezout sono: {x} e {-x+y}")
                print(x)
                print(y)
                y = (-y*lista2[10+incr])+x
                x = x+lista2[10+incr]
            passaggi -= 1
            incr += 4
        else:
            # Se capita di trovare numeri di Bezout che danno zero invece del MCD, è a causa del fatto che:
            # viene tenuta traccia anche dell'ultimo passaggio di Euclide, con lo zero alla fine.
            print("I numeri di Bezout sono veramente:")
            print("^^^^^^^^vedi sopra^^^^^^^^")
            
