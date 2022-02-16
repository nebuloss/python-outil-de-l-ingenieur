#!/bin/python3.8

operation=input("Veuillez saisir la multiplication: ").split("*")

try:
    if len(operation)!=2:
        raise ValueError
    a,b=int(operation[0]),int(operation[1])
except:
    print("erreur de saisie: exemple de saisie: 2*3")
    exit()

var=1
result=0
i=0
while (var<=b):
    if (b&var):
        j=a<<i
        print(var,"*",a,"+")
        result+=j
    var<<=1 
    i+=1
print("=",result)   
