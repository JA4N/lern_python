class Account(object):

    def __init__(self, owner, start=0.0):
        """
        Der Parameter owner ist verpflichtent. Er repräsentiert den Eigentümer eines Kontos.

        Über den Parameter start geben wir an, dass bei der Erzeugung einer Instanz ein Argument übergeben werden kann.
        Sollte bei der Erzeugung kein Argument übergeben werden, wird ein Standardwert (hier: 0.0) gesetzt.
        Anschließend findet eine Zuweisung des Arguments an das Attribut balance statt.
        """
        self.__owner = owner
        self.__balance = start

    def get_balance(self):
        """
        Gibt den aktuellen Kontostand zurück
        :return: den aktuellen Kontostand
        """
        return self.__balance

    def display(self):
        """
        Gibt den aktuellen Kontostand auf der Konsole aus
        """
        print("Balance: {}".format(self.__balance))

    def deposit(self, amount):
        """
        Methode für die Einzahlung auf ein Konto.
        :param amount: Betrag der auf das Konto eingezahlt werden soll.
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Methode für das Abheben eines Betrags von einem Konto.
        :param amount: Betrag der von dem Konto abgehoben werden soll.
        """
        self.__balance -= amount

    def get_owner(self):
        """
        Auslesen des Kontoinhabers.
        :return: Kontoinhaber-Instanz
        """
        return self.__owner

