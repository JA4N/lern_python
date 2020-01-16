from shared.bo.customer import Customer
from server.db.mapper import Mapper
from server.db.account_mapper import AccountMapper
import sqlite3


class CustomerMapper(Mapper):
    """
    Mapper-Klasse, die Customer-Objekte auf eine relationale Datenbank abbildet. Hierzu wird eine Reihe von Methoden
    zur Verfügung gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und gelöscht werden können. Das
    Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.

    Hinweis: Diese Klasse ist analog zur Klasse AccountMapper implementiert.
    """
    def __init__(self):
        """
        Aufruf der init-Methode der Superklasse, um damit das Verbindungsobjekt zur Datenbank zu erhalten.
        """
        super().__init__()

    def find_all(self):
        """
        Auslesen aller Kunden.
        :return: Einw Liste mit Customer-Objekten, die sämtliche Kunden repräsentieren. Bei evtl. Exceptions wird ein
                partiell gefüllter oder ggf. auch leerer Liste zurückgeliefert.
        """
        # Liste für alle Kunden vorbereiten
        result = []
        cursor = self._cnx.cursor()
        try:
            cursor.execute("SELECT id, firstName, lastName from customers")
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Customer-Objekt erstellt.
            for (id, firstName, lastName) in tuples:
                person = Customer()
                person.set_id(id)
                person.set_first_name(firstName)
                person.set_last_name(lastName)
                # Hinzufügen des neuen Objekts zur Ergebnisliste
                result.append(person)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Ergebnisliste zurückgeben
        return result

    def find_by_last_name(self, name):
        """
        Auslesen aller Kunden-Objekte mit gegebenem Nachnamen
        :param name: Nachname der Kunden, die ausgegeben werden sollen
        :return: Eine Liste mit Customer-Objekten, die sämtliche Kunden mit dem gesuchten Nachnamen repräsentieren. Bei
        evtl. Exceptions wird ein partiell gefüllter oder ggf. auch eine leere Liste zurückgeliefert.
        """
        result = []
        cursor = self._cnx.cursor()
        try:
            command = "SELECT id, firstName, lastName FROM customers WHERE lastName LIKE '{}'" \
                      " ORDER BY lastName".format(name)
            cursor.execute(command)
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Customer-Objekt erstellt.
            for (id, firstName, lastName) in tuples:
                person = Customer()
                person.set_id(id)
                person.set_first_name(firstName)
                person.set_last_name(lastName)
                # Hinzufügen des neuen Objekts zur Ergebnisliste
                result.append(person)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Ergebnisliste zurückgeben
        return result

    def find_by_key(self, key):
        """
        Suchen eines Kunden mit vorgegebener Kundennummer. Da diese eindeutig ist, wird genau ein Objekt zurückgegeben.
        :param key: Primärschlüsselattribut (->DB)
        :return: Kunden-Objekt, das dem übergebenen Schlüssel entspricht, None bei nicht vorhandenem DB-Tupel
        """
        cursor = self._cnx.cursor()
        try:
            # Statement ausfüllen und als Query an die DB schicken
            command = "SELECT id, firstName, lastName FROM customers WHERE id={}".format(key)
            cursor.execute(command)
            tuples = cursor.fetchall()
            # Ergebnis-Tupel in Objekt umwandeln
            # Da id Primärschlüssel ist, kann max. nur ein Tupel zurückgegeben werden. Prüfe, ob ein Ergebnis vorliegt.
            (id, firstName, lastName) = tuples[0]
            person = Customer()
            person.set_id(id)
            person.set_first_name(firstName)
            person.set_last_name(lastName)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

        return person

    def insert(self, person):
        """
        Einfügen eines Customer-Objekts in die Datenbank. Dabei wird auch der Primärschlüssel des übergebenen Objekts
        geprüft und ggf. berichtigt.
        :param person: das zu speichernde Objekt
        :return: das bereits übergebene Objekt, jedoch mit ggf. korrigierter id.
        """
        cursor = self._cnx.cursor()
        try:
            # Zunächst schauen wir nach, welches der momentan höchste Primärschlüsselwert ist.
            cursor.execute("SELECT MAX(id) AS maxid FROM customers ")
            tuples = cursor.fetchall()
            # Wenn wir etwas zurückerhalten, kann dies nur einzeilig sein
            (maxid) = tuples[0]
            # person erhält den bisher maximalen, nun um 1 inkrementierten Primärschlüssel.
            person.set_id(maxid[0]+1)
            # Jetzt erst erfolgt die tatsächliche Einfügeoperation
            command = "INSERT INTO customers (id, firstName, lastName) VALUES ({},'{}','{}')" \
                .format(person.get_id(), person.get_first_name(), person.get_last_name())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Rückgabe, des evtl. korrigierten Customers.
        return person

    def update(self, person):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param person: das Objekt, das in die DB geschrieben werden soll
        :return: das als Parameter übergebene Objekt
        """
        try:
            cursor = self._cnx.cursor()

            command = "UPDATE customers " + "SET firstName={}, lastName={} WHERE id={}"\
                .format(person.get_first_name(), person.get_last_name(), person.get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Um Analogie zu insert(Customer c) zu wahren, geben wir c zurück
        return person

    def delete(self, person):
        """
        Löschen der Daten eines Customer-Objekts aus der Datenbank.
        :param person: das aus der DB zu löschende "Objekt"
        :return: None
        """
        cursor = self._cnx.cursor()
        try:
            command = "DELETE FROM customers WHERE id={}".format(person.get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

    def get_accounts_of(self, c):
        """
        Auslesen der zugehörigen Account-Objekte zu einem gegebenen Kunden.
        :param c: der Kunde, dessen Konten wir auslesen möchten
        :return: eine Liste mit sämtlichen Konto-Objekten des Kunden
        """
        """
        Wir bedienen uns hier einfach des AccountMapper. Diesem geben wir einfach den in dem Customer-Objekt enthaltenen
        Primärschlüssel.Der CustomerMapper löst uns dann diese ID in eine Reihe von Konto-Objekten auf.
        """
        a_mapper = AccountMapper()
        a_mapper.find_by_owner_id(c.get_id())


if __name__ == "__main__":
    mapper = CustomerMapper()
    result = mapper.find_all()
    for p in result:
        print(p)
