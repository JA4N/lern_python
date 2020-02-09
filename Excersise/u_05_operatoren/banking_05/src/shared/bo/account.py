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
        # Kreditrahmen
        self.__kreditrahmen = -1500

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
        return self.__kreditrahmen

    def set_credit_line(self, credit_line):
        self.__kreditrahmen = credit_line

    def get_interest(self):
        """
        Berechnen des Zinsertrags.
        :return: Zinsertrag
        """
        return self.get_balance() * (self.get_interest_rate() / 100)

    def is_balance_alert(self):
        #Rechnung für weniger als 5% auf Konto
        erg = self.__balance * 0.05
        if self.__balance < erg:
            return True

    def is_overdraw_amount(self, amount):
        #Zwischenrechnung: Geld wird abgehoben
        erg = self.__balance - amount
        if erg < self.__kreditrahmen:
            return True

    def __str__(self):
        return "Account: {}, owned by {}".format(self.get_id(), self._owner)
