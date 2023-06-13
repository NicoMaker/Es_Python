
print (" ")
print ("----------------------------------- BEZOUL  ----------------------------------- ")

print("")
print ("-------------------------------- SVOLGIMENTO ----------------------------------- ")
print("")

passaggio = 0

def mcd(a, b):
    mcd = 0
    m = a % b
    while m != 0:
        print_euclid(a, b, (a - m) / b, m)
        a = b
        b = m
        mcd = m
        m = a % b
    print_euclid(a, b, (a - m) / b, m)
    print("Il MCD è " + str(mcd) + "\n")


def print_euclid(a, b, c, m):
    print (f"il {passaggio} passaggio è ---->")
    print(" " + str(a) + " = " + str(b) + " * " + str(int(c)) + " + " + str(m))


def bezout(a, b):
    # solve euclid
    terms = []
    m = a % b
    while m != 0:
        c = int((a - m) / b)
        terms.append((m, c * -1, b, 1, a))
        a = b
        b = m
        m = a % b

    # solve bezout
    vals = terms.pop()
    (_mcd, a, x, b, y) = vals
    print_bezout(_mcd, a, x, b, y)
    while len(terms) > 0:
        vals = terms.pop()
        x = vals[4]
        a = a * vals[3]
        b = b + a * vals[1]
        print_bezout(_mcd, a, x, b, y)
        t = a
        a = b
        b = t
        t = x
        x = y
        y = t
        print_bezout(_mcd, a, x, b, y)
    print("Result: " + str(_mcd) + " = " + str(a * x + b * y))
    print("\n")



def print_bezout(mcd_, a, x, b, y):
    sign = " + "
    if b < 0:
        sign = " - "
        b *= -1
    print(str(mcd_) + " = " + str(a) + " * " + str(x) + sign + str(b) + " * " + str(y))
    

#mcd(6172432, 2051143)
#mcd(67981, 3571)
#mcd(3648944, 32487)

bezout(6172432, 2051143)
bezout(67981, 3571)
bezout(3648944, 32487)

print(" ")
print (" ALGORITMO FINITO")
print(" ")
 print (f" Programma fatto in {passaggio} passaggi ")
