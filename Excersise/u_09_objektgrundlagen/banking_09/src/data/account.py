from data.transaction import Transaction


# Klasse der Bankkonten
class Account:

    def __init__(self, owner=None, id=0):
        self.__id = id
        self.__balance = 0.0
        self.__interest_rate = 5.0
        self.__credit_line = -1600.0
        self.__owner = owner
        self.__transactions = []
        self.__transaction_pointer = 0

    """
    Auslesen und setzen der Kontonummer
    """
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    """
    Auslesen und setzen des Kontostands
    """
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    """
    Auslesen und setzen des Zinssatzes
    """
    def get_interest_rate(self):
        return self.get_current_balance() * (self.__interest_rate / 100)

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    """
    Auslesen und setzen des Überziehungsbetrages
    """
    def get_credit_line(self):
        return self.__credit_line

    def set_credit_line(self, credit_line):
        self.__credit_line = credit_line

    """
     Auslesen und setzen des Kontoinhabers
     """
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    """
     Auslesen und setzen der Transaktionen
     """
    def get_transactions(self):
        return self.__transactions

    def set_transactions(self, transactions):
        self.__transactions = transactions

    """
     Auslesen und setzen des Pointers für die Transaktionen
     """
    def get_transaction_pointer(self):
        return self.__transaction_pointer

    def set_transaction_pointer(self, transaction_pointer):
        self.__transaction_pointer = transaction_pointer

    # Eine Einzahlung bzw. Gutschrift für das Konto buchen.
    def make_deposit(self, amount):
        self.__balance += amount

    # Eine Auszahlung bzw. Belastung des Kontos buchen.
    def make_withdrawal(self, amount):
        self.__balance -= amount

    """
    Boolsche Methode zum Abprüfen eines "kritischen"
    Kontostandes, d.h. der Kontostand ist weniger als 1%
    über der Kreditlinie
    """
    def is_balance_alert(self):
        return self.get_current_balance() <= (self.__credit_line - (self.__credit_line / 100))

    """
    Boolsche Methode zum Feststllen, ob das Abheben eins bestimmten
    Betrags den Kontostand unterhalb der Kreditlinie führt.
    """
    def is_overdraw_amount(self, amount):
        return (self.get_current_balance() + amount) <= self.__credit_line

    # Berechnet den aktuellen Kontostand
    def get_current_balance(self):
        current_balance = self.__balance
        for transaction in self.__transactions:
            if transaction is not None:
                current_balance += transaction.amount
        return current_balance

    # Fügt eine Buchung hinzu
    def book(self, amount, text):
        transaction = Transaction()
        transaction.amount = amount
        transaction.text = text
        self.__transactions.append(transaction)
        self.__transaction_pointer += 1

    # Aktualisiert das Attribut balance mit Hilfe der transactions
    def update_balance(self):
        self.__balance = self.get_current_balance()
        self.__transactions = []
        self.__transaction_pointer = 0

    # Gibt den Kontoauszug aus
    def print_account_statement(self):
        temp_balance = self.__balance
        print("Kontoauszug fuer : " + self.__owner.get_first_name() + " " + self.__owner.get_last_name())
        print("Kontonummer      : " + str(self.__id))
        print("\n")
        print("Kontostand zu Beginn: " + str(self.__balance))
        for transaction in self.__transactions:
            temp_balance += transaction.amount
            print(str(transaction.date) + " " + transaction.text + " "
                  + str(transaction.amount) + " " + str(temp_balance))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.id == other.id:
                return True
        return False
