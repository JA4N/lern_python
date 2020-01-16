from abc import ABC


class BusinessObject(ABC):
    """
    Die Klasse BusinessObject stellt die Basisklasse aller in diesem Projekt für die Umsetzung des Fachkonzepts
    relevanten Klassen dar. Zentrales Merkmal ist, dass jedes BusinessObject eine Nummer besitzt, die man in einer
    relationalen Datenbank auch als Primärschlüssel bezeichnen würde.
    """
    def __init__(self):
        # Die eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._id = 0

    def get_id(self):
        """
        Abrufen der Id
        :return: id
        """
        return self._id

    def set_id(self, value):
        """
        Setzen der Id
        :param value: die id
        :return: None
        """
        self._id = value
