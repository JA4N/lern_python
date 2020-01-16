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

    def __str__(self):
        return "Account: {}, owned by {}".format(self.get_id(), self._owner)
