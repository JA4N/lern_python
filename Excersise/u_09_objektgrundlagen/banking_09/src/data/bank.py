class Bank:

    def __init__(self, name=""):
        self.__id = 0
        self.__name = name
        self.__street = ""
        self.__zip = 0
        self.__city = ""
        self.__accounts = []

    """
    Auslesen und setzen der Bankleitzahl
    """
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    """
    Auslesen und setzen des Namens der Bank
    """
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    """
    Auslesen und setzen der Strasse
    """
    def get_street(self):
        return self.__street

    def set_street(self, street):
        self.__street = street

    """
    Auslesen und setzen der Postleitzahl
    """
    def get_zip(self):
        return self.__zip

    def set_zip(self, zip):
        self.__zip = zip

    """
    Auslesen und setzen des Ortes, an dem sich die Bank befindet. 
    """
    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city

    """
    Auslesen und setzen der zu verwaltenden Accounts
    """
    def get_accounts(self):
        return self.__accounts

    def set_accounts(self, accounts):
        self.__accounts = accounts

    # liefert das Konto mit vorgegebener Kontonummer
    def get_account(self, account_number):
        for account in self.__accounts:
            if account.__id == account_number:
                return account
        return None

    # Hinzufügen eines Accounts
    def add_account(self, account):
        self.__accounts.append(account)

    # Gibt Informationen über alle Konten auf dem Bildschirm aus
    def print_accounts(self):
        print(self.__name)
        for account in self.__accounts:
            print("Name : " + account.get_owner().get_first_name() + " " + account.get_owner().get_last_name() +
                  "\t\tKTNO : " + str(account.get_id()) +
                  "\t\tKontostand : " + str(account.get_balance()))
        print("\n")
