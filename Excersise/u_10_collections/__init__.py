#Übungen Listen
#Aufgabe 1
"""
vars = [1, 2]
vars.append(3)
print(vars)
"""
#Aufgabe 2
"""
financialInstitutions = ["Royal Bank of Scotland", "Bradford & Bingley",
                         "Barclays Bank", "Bank of New York", "ING Bank", "Bank of China"]

erg = 0

for zaehler in financialInstitutions:
    if "Barclays Bank" in zaehler:
        print("Gefunden!")
        print(len(financialInstitutions))
        break
    else:
        continue

for zaehler in financialInstitutions:
    print(zaehler)

print(financialInstitutions[4])
"""
#Aufgabe 3
"""
list = [1, 2, 3, 3, 4, 5]

erg = 0
sum = 0
while erg < len(list):
    sum += list[erg]
    erg += 1

print(sum)
"""
#Aufgabe 4
"""
list = [7, 2, 1, 9, 4, 5]

def groesste_zahlen(*args):
    max_number = args[0]
    for number in args:
        if number > max_number:
            max_number = number
    return max_number
c = groesste_zahlen(list)
print(c)
"""
#Aufgabe 5
"""
zeichen = ['H', 'D', 'M']

def zusammenfügen(liste):
    leerer_string = ""
    for zaehler in liste:
        leerer_string += zaehler
    return leerer_string
"""
#Übungen Tuple
#Aufgabe 1
"""
tuple = (1, 2, 3, 4, 5)
print(tuple[2])
"""
#Aufgabe 2
"""
tuple = (1, 2, 3, 4, 5, 6)
tuple += (7,)
print(tuple)
"""
#Aufgabe 3
"""
tuple=("Jan", "Ines", "Heinz", "Jürgen")
def get_length(*args):
    return len(args)

print(get_length(tuple))
"""
#Aufgabe 4
"""
tuple=("Jan", "Ines", "Heinz", "Jürgen")

def untersuchen(tuple):
    for c in tuple:
        if c == "Jan":
            print("vorhanden")
        else:
            print("nicht vohanden")

print(untersuchen(tuple))
"""
"""
def untersuchen(tuple, item):
    return item in tuple
print(untersuchen(tuple))
"""
#Aufgabe 5
"""
list = [1, 2, 3, 4, 5]

def list_to_tuple(list_to_convert):
    zaehler = 0
    tuple = ()
    while zaehler < len(list_to_convert):
        tuple += list_to_convert[zaehler]
        zaehler += 1
    return tuple

print(list_to_tuple(list))
"""
#Aufgabe 6
"""
tuple = ("Herbert Müller", 22348,
             "Erna Sparbier", 23409,
             "Sandra Schweigmeier", 33007,
             "Konrad Adenauer", 35279,
             "Helmut Schmidt", 27431,
             "Ludwig Erhard", 35803)

def tuple_to_dict(tuple_to_convert):
    result = list()
    i = 0
    while i < len(tuple_to_convert):
        tmp = {tuple_to_convert[i+1]:tuple_to_convert[i]}
        i += 2
        result.append(tmp)
    return result

print(tuple_to_dict(tuple))
"""
