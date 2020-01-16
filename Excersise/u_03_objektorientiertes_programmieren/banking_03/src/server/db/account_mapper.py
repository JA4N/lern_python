from shared.bo.account import Account
from server.db.mapper import Mapper
import sqlite3


class AccountMapper(Mapper):
    """
    Mapper-Klasse, die Account-Objekte auf eine relationale Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur
    Verfügung gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und gelöscht werden können. Das
    Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        """
        Aufruf der init-Methode der Superklasse, um damit das Verbindungsobjekt zur Datenbank zu erhalten.
        """
        super().__init__()

    def find_all(self):
        """
        Eine Beispielmethoden, die alle Tupel ausliest und als Objekte zurückgibt.
        :return: Eine Liste mit Account-Objekten, die sämtliche Konten repräsentieren.
        Bei evtl. Exceptions wird ein partiell gefüllter oder ggf. auch leerer Vetor zurückgeliefert.
        """
        result = []
        try:
            cursor = self._cnx.cursor()
            cursor.execute("SELECT id, owner from accounts")
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Account-Objekt erstellt.
            for (id, owner) in tuples:
                account = Account()
                account.set_id(id)
                account.set_owner(owner)
                # Hinzufügen des neuen Objekts zum Ergebnis
                result.append(account)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Ergebnis zurückgeben
        return result

    def find_by_owner_id(self, owner_id):
        """
        Auslesen aller Konten eines durch Fremdschlüssel (Kundennr.) gegebenen
        Kunden.
        :param owner_id: Schlüssel des zugehörigen Kunden.
        :return: Einw Liste mit Account-Objekten, die sämtliche Konten des betreffenden Kunden repräsentieren.
        Bei evtl. Exceptions wird ein partiell gefüllter oder ggf. auch leerer Vetor zurückgeliefert.
        """
        result = []
        try:
            cursor = self._cnx.cursor()
            command = "SELECT id, owner FROM accounts WHERE owner={} ORDER BY id".format(owner_id)
            cursor.execute(command)
            tuples = cursor.fetchall()

            # Für jeden Eintrag im Suchergebnis wird nun ein Account-Objekt erstellt.
            for (id, owner) in tuples:
                account = Account()
                account.set_id(id)
                account.set_owner(owner)
                # Hinzufügen des neuen Objekts zum Ergebnis
                result.append(account)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Ergebnis zurückgeben
        return result

    def find_by_key(self, key):
        """
        Suchen eines Kontos mit vorgegebener Kontonummer. Da diese eindeutig ist, wird genau ein Objekt zurückgegeben.
        :param key: Primärschlüsselattribut (->DB)
        :return: Konto-Objekt, das dem übergebenen Schlüssel entspricht, None bei nicht vorhandenem DB-Tupel.
        """
        cursor = self._cnx.cursor()
        try:
            # Statement ausfüllen und als Query an die DB schicken
            command = "SELECT id, owner FROM accounts WHERE id={}".format(key)
            cursor.execute(command)
            tuples = cursor.fetchall()

            # Da id Primärschlüssel ist, kann max. nur ein Tupel zurückgegeben werden. Prüfe, ob ein Ergebnis vorliegt.
            (id, owner) = tuples[0]
            account = Account()
            account.set_id(id)
            account.set_owner(owner)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        return account

    def insert(self, account):
        """
        Einfügen eines Account-Objekts in die Datenbank. Dabei wird auch der Primärschlüssel des übergebenen Objekts
        geprüft und ggf. berichtigt.
        :param account: das zu speichernde Objekt
        :return: das bereits übergebene Objekt, jedoch mit ggf. korrigierter id
        """
        cursor = self._cnx.cursor()
        try:
            # Zunächst schauen wir nach, welches der momentan höchste Primärschlüsselwert ist.
            cursor.execute("SELECT MAX(id) AS maxid FROM accounts ")
            tuples = cursor.fetchall()

            (maxid) = tuples[0]
            # a erhält den bisher maximalen, nun um 1 inkrementierten Primärschlüssel.
            account.set_id(maxid[0] + 1)

            # Jetzt erst erfolgt die tatsächliche Einfügeoperation
            command = "INSERT INTO accounts (id, owner) VALUES ({},{})" \
                .format(account.get_id(), account.get_owner().get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()

        # Rückgabe, des evtl. korrigierten Accounts.
        return account

    def update(self, account):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param account:d as Objekt, das in die DB geschrieben werden soll
        :return: das als Parameter übergebene Objekt
        """
        cursor = self._cnx.cursor()
        try:
            command = "UPDATE accounts SET owner={} WHERE id={}".format(account.get_owner(), account.get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Um Analogie zu insert(Account a) zu wahren, geben wir a zurück
        return account

    def delete(self, account):
        """
        Löschen der Daten eines Account-Objekts aus der Datenbank.
        :param account: das aus der DB zu löschende "Objekt"
        :return: None
        """
        cursor = self._cnx.cursor()
        try:
            command = "DELETE FROM accounts WHERE id={}".format(account.get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()


if __name__ == "__main__":
    mapper = AccountMapper()
    result = mapper.find_all()
    for p in result:
        print(p)