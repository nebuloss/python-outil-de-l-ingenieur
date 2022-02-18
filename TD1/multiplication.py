#!/bin/python3.8
#Guillaume Chayé

operation=input("Veuillez saisir la multiplication: ").split("*")

try:
    if len(operation)!=2:
        raise ValueError
    a,b=int(operation[0]),int(operation[1])
except:
    print("erreur de saisie: exemple de saisie: 2*3")
    exit()

var=1
copy=a
result=0
while var<=b:
    if var&b:
        result+=a
        print(var,"*",copy,"+")
    a=a+a
    var=var+var

print("=",result)


