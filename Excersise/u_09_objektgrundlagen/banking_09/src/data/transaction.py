import datetime


# Klasse der Bankkonten
class Transaction:

    """
    Attribute der Klasse
    """
    __slots__ = ['__amount', '__text', '__date']

    def __init__(self):
        self.__amount = 0.0
        self.__text = ""
        self.__date = datetime.datetime.now()

    """
    Auslesen und setzen der Buchungsmenge
    """
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    """
    Auslesen und setzen des Verwendungszwecks
    """
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    """
    Auslesen und setzen des Erstellungsdatums
    """
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date
