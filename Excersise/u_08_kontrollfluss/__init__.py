#Aufgabe 2
"""""
liste = ["Hochschule", "der", "TEST", "Medien"]
gesuchtNach = "Medien"
zaehler = 0
gefunden = False

while zaehler < len(liste):
    if liste[zaehler] == gesuchtNach:
        gefunden = True
        break
    zaehler += 1

if gefunden == True:
    print("Gefunden! Nach dem " + str(zaehler) + " durchgang")
else:
    print("nicht gefunden")
"""""
#Aufgabe 3
""""
list = [1, 2, 3, 4, 5, 6]
list2 = []
zaehler = 0
kontrolle = 3, 6

while zaehler < len(list):
    if list[zaehler] != kontrolle:
        list2.append(list[zaehler])
    else:
        continue
    zaehler += 1

print(list2)
"""
#Aufgabe 5
"""
listNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
geradeZahl = 0
ungeradeZahl = 0
zaehler = 0

while zaehler < len(listNumbers):
    erg = listNumbers[zaehler] % 2
    if erg != 0:
        ungeradeZahl += 1
    elif erg == 0:
        geradeZahl += 1
    zaehler += 1

print("Gerade Zahlen: " + str(geradeZahl))
print("Ungerade Zahlen: " + str(ungeradeZahl))
"""
