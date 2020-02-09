#Aufgabe 1
"""
def sum_up(*args):
    erg = 0
    for x in args:
        erg += x
    return erg

c = sum_up(2, 3, 4, 5, 6,)
print(c)
"""
#Aufgabe 2
"""
def multiply(*args):
    erg = 1
    for x in args:
        erg *= x
    return erg

d = multiply(1,2,3,3)
print(d)
"""
#Aufgabe 3
"""
def is_range(number, start, end):
    if number < end and number > start:
        print("Die Zahl " + str(number) + " liegt zwischen " + str(start) + " und " + str(end))
    elif number > end:
        print("Die Zahl ist out of range")
    elif number < start:
        print("die Zahl ist kleiner")
    else:
        print("Die Zahl ist genauso Groß")

a = input("Größste Zahl")
b = input("Kleinste Zahl")
c = input("Zu prüfende Zahl")

erg = is_range(c, b, a)
"""
#Aufgabe 4
"""
def find_max(x, y, z):
    erg = find_max_between_two(x, y)
    if erg > z:
        return erg
    else:
        return z

def find_max_between_two(x, y):
        if x > y:
            return x
        else:
            return y

a = input("Bitte die erste Zahl eingeben")
b = input("Bitte die zweite Zahl eingeben")
c = input("Bitte die dritte Zahl eingeben")

print("Die Größte der eingegebenen Zahlen ist: " + find_max(a, b, c))
"""
#Aufgabe 5
"""
def find_max_of_list(*args):
    max = args[0]
    for value in args:
        if value > max:
            max = value
    return max

print(find_max_of_list(1, 2, 3, 4, 5, 6, 7, 32, 4, 6))
"""
#Aufgabe 6
"""
c = input("Geben Sie einen Text ein")
def berechne(text):
    großbuchstaben = 0;
    kleinbuchstaben = 0;
    for berechnen in text:
        if berechnen.isupper() == True:
            großbuchstaben += 1
        elif berechnen.islower() == True:
            kleinbuchstaben+= 1
        else:
            print("Was zur Hölle hast du eingegeben?")
    print("Originaltext: " + text)
    print("Anzahl Großbuchstaben: " + str(großbuchstaben))
    print("Anzahl Kleinbuchstaben: " + str(kleinbuchstaben))
"""
