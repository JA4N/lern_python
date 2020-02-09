from data.customer import Customer
from data.account import Account
from data.bank import Bank

"""
Übung 09 - Aufgabe 1
Beheben Sie die Fehler im Code!
"""

my_first_account = Account()
my_first_account.owner = Customer("Sina", "Sappel")
print("Kontoeigentümer : " + my_first_account.get_owner())
print("Kontonummer     : " + my_first_account.get_id())
print("Kreditrahmen    : " + my_first_account.get_credit_line())
print("Zinssatz        : " + my_first_account.get_interest_rate())
print("Kontostand      : " + my_first_account.get_current_balance())

"""
Übung 09 - Aufgabe 2
Welche Objekte können nach Ausführung des folgenden Codes vom
Garbage Collector gelöscht werden? Begründen Sie!
"""
my_first_bank = Bank("Spar Nix Bank AG")
my_second_account = Account(Customer("Sina", "Sappel"), 2345)
my_first_bank.add_account(my_second_account)
my_second_account = None

"""
Übung 09 - Aufgabe 4
Welche Fehler enthält der folgende Code?
"""
my_third_account = Account(Customer("Bodo", "Bank"), 2346)
my_third_account.update_balance = 5678.90
my_balance = my_third_account.balance()

"""
Übung 09 - Aufgabe 5
Welchen Wert ergibt der folgende Ausdruck:
myFourthAccount is myFifthAccount?
Begründen Sie!
"""
paul_ahner = Customer("Paul", "Ahner")
my_fourth_account = Account(paul_ahner, 2000)
my_fifth_account = Account(paul_ahner, 2000)
print(my_fourth_account is my_fifth_account)

"""
Übung 09 - Aufgabe 6
Fügen Sie bitte hier Ihren eigenen Code ein:
"""
