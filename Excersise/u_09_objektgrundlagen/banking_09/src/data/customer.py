# Klasse der Bankkunden
class Customer:

    def __init__(self, first_name="", last_name=""):
        self.__id = 0
        self.__last_name = last_name
        self.__first_name = first_name

    """
    Auslesen und setzen der Kundennummer
    """
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    """
    Auslesen und setzen des Vornamens
    """
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    """
    Auslesen und setzen des Nachnamens
    """
    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def __str__(self):
        return self.__first_name + " " + self.__last_name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__id == other.id:
                return True
        return False

    def __hash__(self):
        seed = 7
        seed *= 79 + hash(self.__first_name)
        seed *= 79 + hash(self.__last_name)
        seed *= 79 + self.__id
        return seed
