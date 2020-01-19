from shared.bo.customer import Customer
from shared.bo.account import Account
from shared.bo.transaction import Transaction

from server.db.customer_mapper import CustomerMapper
from server.db.account_mapper import AccountMapper
from server.db.transaction_mapper import TransactionMapper

import datetime


class BankAdministration:
    """
    Diese Klasse ist die Klasse, die sämtliche Applikationslogik (oder engl. Business Logic) aggregiert. Sie ist
    wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
    dauerhafte Konsistenz der Daten und Abläufe sorgt.
    Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
    Methoden kann als Transaction Script bezeichnet werden. Dieser Name
    lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
    Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
    von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
    Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
    jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
    durchzuführen.

    Wichtiger Hinweis: Diese Klasse bedient sich sogenannter
    Mapper-Klassen. Sie gehören der Datenbank-Schicht an und bilden die
    objektorientierte Sicht der Applikationslogik auf die relationale
    organisierte Datenbank ab. Zuweilen kommen "kreative" Zeitgenossen auf die
    Idee, in diesen Mappern auch Applikationslogik zu realisieren. Einzig nachvollziehbares
    Argument für einen solchen Ansatz ist die Steigerung der Performance
    umfangreicher Datenbankoperationen. Doch auch dieses Argument zieht nur dann,
    wenn wirklich große Datenmengen zu handhaben sind. In einem solchen Fall
    würde man jedoch eine entsprechend erweiterte Architektur realisieren, die
    wiederum sämtliche Applikationslogik in der Applikationsschicht isolieren
    würde. Also, keine Applikationslogik in die Mapper-Klassen "stecken" sondern
    dies auf die Applikationsschicht konzentrieren!
    """
    def __init__(self):
        """
        Ganz wesentlich ist, dass die BankAdministration einen vollständigen Satz
        von Mappern besitzt, mit deren Hilfe sie dann mit der Datenbank kommunizieren kann.
        """
        self.__customer_mapper = CustomerMapper()
        self.__account_mapper = AccountMapper()
        self.__transaction_mapper = TransactionMapper()

    """
    Customer-spezifische Methoden
    """
    def create_customer(self, first_name, last_name):
        """
        Anlegen eines neuen Kunden. Dies führt implizit zu einem Speichern des neuen Kunden in der Datenbank.
        HINWEIS: Änderungen an Customer-Objekten müssen stets durch Aufruf
        save(Customer c) in die Datenbank transferiert werden.
        :param first_name: Vorname des Kunden
        :param last_name: Nachname des Kunden
        :return: Kundenobjekt
        """
        customer = Customer()
        customer.set_first_name(first_name)
        customer.set_last_name(last_name)
        # Setzen einer vorläufigen Kundennr. Der insert-Aufruf liefert dann ein Objekt,
        # dessen Nummer mit der Datenbank konsistent ist.
        customer.set_id(1)
        # Objekt in der DB speichern.
        return self.__customer_mapper.insert(customer)

    def get_customer_by_name(self, last_name):
        """
        Auslesen aller Kunden, die den übergebenen Nachnamen besitzen.
        :param last_name: Nachname der gesuchten Kunden
        :return: Alle Kunden mit dem entsprechenden Nachnamen
        """
        return self.__customer_mapper.find_by_last_name(last_name)

    def get_customer_by_id(self, id):
        """
        Auslesen eines Kunden anhand seiner Kundennummer.
        :param id: Id des Kunden
        :return: Kunde der zu der Id gehört
        """
        return self.__customer_mapper.find_by_key(id)

    def get_account_by_id(self, id):
        """
        Auslesen eines Kontos anhand der Kontonummer.
        :param id: Kontonummer
        :return: Das Konto
        """
        return self.__account_mapper.find_by_key(id)

    def get_all_customers(self):
        """
        Auslesen aller Kunden.
        :return: alle Kunden aus der Datenbank
        """
        return self.__customer_mapper.find_all()

    def save_customer(self, customer):
        """
        Speichern eines Kunden.
        :param customer: Kunde der gespeichert werden soll
        :return: None
        """
        self.__customer_mapper.update(customer)

    def delete_customer(self, customer):
        """
        Löschen eines Kunden. Natürlich würde ein reales System zur Verwaltung von Bankkunden ein Löschen allein schon
        aus Gründen der Dokumentation nicht bieten, sondern deren Status z.B von "aktiv" in "ehemalig" ändern.
        Wir wollen hier aber dennoch zu Demonstrationszwecken eine Löschfunktion vorstellen.
        :param customer: der zu löschende Kunde
        :return: None
        """
        
        """
        Zunächst werden sämtl. Konten des Kunden aus der DB entfernt.
    
        Beachten Sie, dass wir dies auf Ebene der Applikationslogik, konkret: in der Klasse BankAdministration, 
        durchführen. Grund: In der Klasse BankAdministration ist die Verflechtung sämtlicher Klassen bzw. ihrer Objekte 
        bekannt. Nur hier kann sinnvoll ein umfassender Verwaltungsakt wie z.B. dieser Löschvorgang realisiert werden.
    
        Natürlich könnte man argumentieren, dass dies auch auf Datenbankebene (sprich: mit SQL) effizienter möglich ist. 
        Das Gegenargument ist jedoch eine dramatische Verschlechterung der Wartbarkeit Ihres Gesamtsystems durch einen 
        zu niedrigen Abstraktionsgrad und der Verortung von Aufgaben an einer Stelle (Datenbankschicht), 
        die die zuvor genannte Verflechtung nicht umfänglich kennen kann.
        """
        accounts = self.__account_mapper.find_by_owner_id(customer.get_id())
        if not (accounts is None):
            for a in accounts:
                self.__account_mapper.delete(a)
        # Anschließend den Kunden entfernen
        self.__customer_mapper.delete(customer)

    """
    Account-spezifische Methoden
    """

    def get_all_accounts(self):
        """
        Auslesen sämtlicher Konten dieses Systems.
        :return: alle Konten
        """
        return self.__account_mapper.find_all()

    def get_accounts_of_customer(self, customer):
        """
        Auslesen aller Konten des übergeben Kunden.
        :param customer: Kunde dessen Konten gesucht werden
        :return: alle Konten des Kunden
        """
        accounts = self.__account_mapper.find_by_owner_id(customer.get_id())

        return accounts

    def delete_account(self, account):
        """
        Löschen des übergebenen Kontos. Beachten Sie bitte auch die Anmerkungen zu delete(Customer).
        Beim Löschen des Kontos werden sämtliche damit in Verbindung stehenden Buchungen gelöscht.
        :param account: das zu löschende Konto
        :return: None
        """
        # Zunächst werden sämtl. Buchungen des Kunden aus der DB entfernt.
        debits = self.get_debits_of_account(account)
        credits = self.get_credits_of_account(account)

        if not (debits is None):
            for transaction in debits:
                self.delete_transaction(transaction)

        if not (credits is None):
            for transaction in credits:
                self.delete_transaction(transaction)
        # Account aus der DB entfernen
        self.__account_mapper.delete(account)

    def create_account_for_customer(self, customer):
        """
        Anlegen eines neuen Kontos für den übergebenen Kunden. Dies führt implizit zu einem Speichern des neuen,
        leeren Kontos in der Datenbank.

  
        HINWEIS: Änderungen an Account-Objekten müssen stets durch Aufruf von save(Account) in die
        Datenbank transferiert werden.
        :param customer: Kunde für den ein Konto eröffnet wird.
        :return: Das neue Konto
        """
        account = Account()
        account.set_owner(customer)
        # Setzen einer vorläufigen Kontonr. Der insert-Aufruf liefert dann ein Objekt,
        # dessen Nummer mit der Datenbank konsistent ist.
        account.set_id(1)
        # Objekt in der DB speichern
        return self.__account_mapper.insert(account)

    def get_balance_of_account(self, account):
        """
        Ausgeben des Kontostands des übergebenen Kontos. Dieser wird durch ein gegeneinander Aufrechnen von Zubuchungen
        und Abbuchungen auf Basis von Transaction-Instanzen bestimmt.
        :param account: Konto für den der Kontostand abgerufen wird
        :return: Kontostand
        """
        credit_amount = 0
        debit_amount = 0

        debits = self.get_debits_of_account(account)
        credits = self.get_credits_of_account(account)

        if not (debits is None):
            for transaction in debits:
                debit_amount += transaction.get_amount()

        if not (credits is None):
            for transaction in credits:
                credit_amount += transaction.get_amount()

        return credit_amount - debit_amount

    def get_debits_of_account(self, account):
        """
        Auslesen sämtlicher mit diesem Konto in Verbindung stehenden Soll-Buchungen.
        Diese Methode wird in getBalanceOf(Account) verwendet.
        :param account: das Konto, dessen Soll-Buchungen wir bekommen wollen.
        :return: eine Liste aller Soll-Buchungen
        """
        result = []

        if not (account is None):
            transactions = self.__transaction_mapper.find_by_source_account_id(account.get_id())
            if not (transactions is None):
                result.extend(transactions)

        return result

    def get_credits_of_account(self, account):
        """
        Auslesen sämtlicher mit diesem Konto in Verbindung stehenden Haben-Buchungen.
        Diese Methode wird in getBalanceOf(Account) verwendet.
        :param account: das Konto, dessen Haben-Buchungen wir bekommen wollen.
        :return: eine Liste aller Haben-Buchungen
        """
        result = []

        if not (account is None):
            transactions = self.__transaction_mapper.find_by_target_account_id(account.get_id())
            if not (transactions is None):
                result.extend(transactions)

        return result

    def save_account(self, account):
        """
        Speichern eines Kontos.
        :param account: Konto, das gespeichert werden soll
        :return: das Kontoobjekt
        """
        self.__account_mapper.update(account)

    """
    Transaction-spezifische Methoden
    """

    def delete_transaction(self, transaction):
        """
        Löschen der übergebenen Buchung
        :param transaction: die zu löschende Transaktion
        :return: None
        """
        self.__transaction_mapper.delete(transaction)


if __name__ == "__main__":
    adm = BankAdministration()
    customers = adm.get_all_customers()
    for c in customers:
        print(c)
