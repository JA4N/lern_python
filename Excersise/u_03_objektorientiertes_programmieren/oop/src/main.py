"""
Um Objekte vom Typ Customer oder Account zu erzeugen, müssen die Klassen aus den Modulen importiert werden
"""
from customer import Customer
from account import Account

""""
Es wird eine Instanz vom Typ "Customer" erzeugt. Die Init-Methode erwartet zwei Strings:
1. Vorname
2. Nachname
Diese beiden Strings müssen beim erzeugen mitgegeben werden. Ansonsten wird eine Exception geschmissen.
Wenn die Klammern leer bleiben wird eine Instanz von "Customer" ohne parameter erzeugt.
"""
c = Customer("Max", "Mustermann")
"""
Es wird nur der Vorname überschrieben. Die Standartwerde sind in der __init__ im Rumpf angegeben
"""
customer1 = Customer("Jan")
print(customer1.get_first_name())
print(customer1.get_last_name())

customer2 = Customer("John", "Mayer", "12.04.1942")
print(customer2.getgeburtstag())


customer3 = Customer()
customer3.set_first_name("Helmut")
print(customer3.get_first_name())

account2 = Account(customer2, 100)
print(account2.get_balance())
print(account2.get_owner())
print(customer2.get_first_name())
"""
In der Init-Methode von "Account" gibt es den Parameter "owner" vom Typ Customer
"""
a1 = Account(c)
a1.display()
"""
Es wird der Wert 100 in die Variable Balance geschrieben und mit der "display"- Funktion auf der Konsole ausgegeben.
"""
a1.deposit(100.0)
"""
"display" ist eine eigene Methode in "Account" mit einer speziellen Formatierung
"""
a1.display()
"""
Es wird vom Objekt "a1" der Kontostand genommen und auf der Konsole ausgegeben
"""
print(a1.get_balance())
"""
Es wird die Referenz des Objektes angezeigt
"""
print(a1)
print(c)

# Ihr Code
#Kunde erzeugen mit übergebenen Parametern
customer1 = Customer("Hildegard", "Mustermann")
#Konto erzeugen und eien Kunden eintragen -> customer1
konto1 = Account(customer1)

"""
Wünschenswert wäre eine Historie, was für Aktionen am konto durchgeführt wurden.
Außerdem soll die möglichkeit bestehen ein Dispo bis zu einer bestimmten Summe + Zinsen zu bekommen
"""