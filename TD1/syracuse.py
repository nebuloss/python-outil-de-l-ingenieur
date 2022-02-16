#!/bin/python3.8

try:
    nb=int(input("veuillez saisir le nombre départ: "))
except:
    print("erreur de saisie")
    exit()

print("Conjecture de Syracuse")
i=0
checked=False
while True:
    print(nb)
    if nb==1:
        if checked:
            break
        checked=True
    
    if (nb&1):
        nb*=3
        nb+=1
    else:
        nb>>=1
    if not checked:
        i+=1



print("on est arrivé à 1 au bout de {} itérations".format(i))