"""
Um Objekte vom Typ Customer oder Account zu erzeugen, müssen die Klassen aus den Modulen importiert werden
"""
from customer import Customer
from account import Account

c = Customer("Max", "Mustermann")
a1 = Account(c)
a1.display()
a1.deposit(100.0)
a1.display()
print(a1.get_balance())
print(a1)
print(c)

# Ihr Code
