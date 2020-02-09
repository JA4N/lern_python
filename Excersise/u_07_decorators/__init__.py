#Aufgabe 1
""""
def test(func):
    def rechner(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise Exception("Keine natürliche Zahl")
    return rechner

@test
def factorial(n):
    num = 1
    while n >= 1:
        num *= n
        n -= 1
    return num

c = factorial(-1)
"""
#Aufgabe 2

def zaehler(func):
    def zaehlen(x):
        zaehlen.calls += 1
        return func(x)
    zaehlen.calls = 0
    return zaehlen


@zaehler
def succ(x):
    return x+1
for i in range(10):
    succ(i)
