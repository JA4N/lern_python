class Customer:

    def __init__(self, vorname="Max", nachname="Lindheimer", geburtstag = "00.00.0000"):
        # Vorname des Kunden
        self.__first_name = vorname
        # Nachname des Kunden
        self.__last_name = nachname
        # Geburtstag des Kunden
        self.__geburtstag = geburtstag

    def get_first_name(self):
        """
        Vornamen auslesen
        :return: Vorname des Kunden
        """
        return self.__first_name

    def set_first_name(self, vorname):
        """
        Setzen des Vornamens
        :param vorname: Vorname
        :return: None
        """
        self.__first_name = vorname

    def get_last_name(self):
        """
        Nachname auslesen
        :return: Nachname des Kunden
        """
        return self.__last_name

    def set_last_name(self, nachname):
        """
        Setzen des Nachnamens
        :param nachname: Nachname
        :return: None
        """
        self.__last_name = nachname

    def getgeburtstag (self):
        return self.__geburtstag
