from shared.bo import business_object as bo


class Customer (bo.BusinessObject):
    """
    Klasse der Bankkunden
    """
    def __init__(self):
        super().__init__()
        # Vorname des Kunden
        self._first_name = ""
        # Nachname des Kunden
        self._last_name = ""

    def get_first_name(self):
        """
        Vornamen auslesen
        :return: Vorname des Kunden
        """
        return self._first_name

    def set_first_name(self, value):
        """
        Setzen des Vornamens
        :param value: Vorname
        :return: None
        """
        self._first_name = value

    def get_last_name(self):
        """
        Nachname auslesen
        :return: Nachname des Kunden
        """
        return self._last_name

    def set_last_name(self, value):
        """
        Setzen des Nachnamens
        :param value: Nachname
        :return: None
        """
        self._last_name = value

    def __str__(self):
        return "Person: {}, {} {}".format(self.get_id(), self._first_name, self._last_name)
