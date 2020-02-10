from shared.bo import business_object as bo


class Transaction (bo.BusinessObject):
    """
    Klasse der Bankkunden
    """
    def __init__(self):
        super().__init__()
        # Quellkonto
        self._sourceAccount = None
        # Zielkonto
        self._targetAccount = None
        # Betrag
        self._amount = 0.0
        # Buchungstext
        self._text = ""
        # Datum
        self._date = ""

    def get_source_account(self):
        """
        Gibt das Quellkonto zurück
        :return: Quellkonto
        """
        return self._sourceAccount

    def set_source_account(self, account):
        """
        Setzen des Quellkontos
        :param account: Quellkonto
        :return: None
        """
        self._sourceAccount = account

    def get_target_account(self):
        """
        Gibt das Zielkonto zurück
        :return: Zielkonto
        """
        return self._targetAccount

    def set_target_account(self, account):
        """
        Setzen des Zielkontos
        :param account: Zielkonto
        :return: None
        """
        self._targetAccount = account

    def get_amount(self):
        """
        Gibt den Betrag zurück
        :return: Betrag
        """
        return self._amount

    def set_amount(self, amount):
        """
        Setzen des Betrag
        :param amount: Betrag
        :return: None
        """
        self._amount = amount

    def get_text(self):
        """
        Gibt den Buchungstext zurück
        :return: Buchungstext
        """
        return self._text

    def set_text(self, text):
        """
        Setzen des Buchungstextes
        :param text: Buchungstextes
        :return: None
        """
        self._text = text

    def get_date(self):
        """
        Abrufen des Datums
        :return: Das Datum der Buchung
        """
        return self._date

    def set_date(self, date):
        """
        Setzen des Datums
        :param date: Datum
        :return: None
        """
        self._date = date
