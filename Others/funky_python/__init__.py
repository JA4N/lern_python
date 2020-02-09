#Aufgabe 1
"""""
for x in range(101):
    print(x)
    x+= 1
"""
#Aufgabe 2
"""""
def sum(*args):
    for zahl in args:
        if args == 0:
            print(zahl)
            return zahl
        else:
            zahl += args

zahl= sum(1, 2, 3, 0)
"""
