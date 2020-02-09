from shared.bo import business_object as bo


class Account (bo.BusinessObject):
    """
    Realisierung eines exemplarischen Bankkontos. Ein Konto besitzt einen Inhaber sowie eine Reihe von Buchungen
    (vgl. Klasse Transaction), mit deren Hilfe auch der Kontostand berechnet werden kann.
    """
    def __init__(self):
        super().__init__()
        # Eigentümer des Kontos
        self._owner = None
        # Zinssatz
        self.__interest_rate = 5.0
        # Kontostand
        self.__balance = 0.0
        # Überziehungsbetrag
        self.__credit_line = -1500.0
        self.__transactions = []

    def get_owner(self):
        """
        Auslesen des Kontoinhabers.
        :return: Kontoinhaber-Instanz
        """
        return self._owner

    def set_owner(self, person):
        """
        Setzen des Kontoinhabers
        :param person: Inhaber
        :return: None
        """
        self._owner = person

    def get_interest_rate(self):
        """
        Gibt den aktuellen Kreditrahmen zurück
        :return: den Kreditrahmen
        """
        return self.__interest_rate

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        """
        Setzen des Kontostands
        :param balance: neuer Kontostand
        :return: None
        """
        self.__balance = balance

    def get_credit_line(self):
        """
        Rückgabe der Kreditlinie
        :return: Kreditlinie
        """
        return self.__credit_line

    def set_credit_line(self, credit_line):
        """
        Setzen der Kreditlinie.
        :param credit_line: neue Kreditlinie
        :return: None
        """
        self.__credit_line = credit_line

    def get_interest(self):
        """
        Berechnen des Zinsertrags.
        :return: Zinsertrag
        """
        return self.get_balance() * (self.get_interest_rate() / 100)

    def get_transactions(self):
        return self.__transactions
    def set_transactions(self, transactions):
        """
        setzt die Transaktionen
        :param transactions: Transaktionen des Kontos
        :return: None
        """
        self.__transactions = transactions

    def add_transaction(self, transaction):
        """
        fügt den bisherigen Transaktionen eine weitere Buchung hinzu
        :param transaction: Überweisung die hinuzgefügt werden soll
        :return: None
        """
        self.__transactions.append(transaction)

    def is_balance_alert(self):
        """
        Boolsche Methode zum Abprüfen eines "kritischen"
        Kontostandes, d.h. der Kontostand ist weniger als 1%
        über der Kreditlinie
        :return: True, wenn es im kritischen Bereich ist, sonst False
        """
        return self.get_balance() <= (self.get_credit_line() - (self.get_credit_line() / 100))

    def is_overdraw_amount(self, amount):
        """
        Boolsche Methode zum Feststllen, ob das Abheben eins bestimmten
        Betrags den Kontostand unterhalb der Kreditlinie führt.
        :param: amount: Betrag der abgehoben werden soll
        :return: True, wenn es im Kreditrahmen liegt, sonst False
        """
        return (self.get_balance() + amount) <= self.get_credit_line()

    def __str__(self):
        return "Account: {}, owned by {}".format(self.get_id(), self._owner)

    def print_account_statement(self):
        try:
            print(self.get_owner() + "/n")
            print(self.get_id() + "/n")
            print(self.get_balance() + "/n")
            #Alle Transaktionen
            for t in self.get_transactions():
                print(t.get_date())
                print(t.get_Text())
                print(t.get_amount())
                print(t.get_source_account())
                print(t.get_target_account())
        except:
            raise Exception("Fehler beim Drucken des Kontoauszuges")


