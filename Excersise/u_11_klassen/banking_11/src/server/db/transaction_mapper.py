from shared.bo.transaction import Transaction
from server.db.mapper import Mapper
import sqlite3


class TransactionMapper (Mapper):
    """
    Mapper-Klasse, die Transation-Objekte auf eine relationale Datenbank abbildet. Hierzu wird eine Reihe von Methoden
    zur Verfügung gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und gelöscht werden können. Das
    Mapping ist bidirektional. D.h., Objekte können in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        """
        Aufruf der init-Methode der Superklasse, um damit das Verbindungsobjekt zur Datenbank zu erhalten.
        """
        super().__init__()

    def find_all(self):
        """
        Auslesen aller Buchungen.
        :return: Eine Liste mit Transaction-Objekten, die sämtliche Buchungen repräsentieren. Bei evtl. Exceptions wird
        ein partiell gefüllter oder ggf. auch leere Liste zurückgeliefert.
        """
        result = []
        cursor = self._cnx.cursor()
        try:
            cursor.execute("SELECT id, sourceAccount, targetAccount, amount, text, date from transactions")
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Transaktion-Objekt erstellt.
            for (id, source_account, target_account, amount, text, date) in tuples:
                transaction = Transaction()
                transaction.set_id(id)
                transaction.set_source_account(source_account)
                transaction.set_target_account(target_account)
                transaction.set_amount(amount)
                transaction.set_text(text)
                transaction.set_date(date)
                # Hinzufügen des neuen Objekts zur Liste
                result.append(transaction)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Liste zurückgeben
        return result

    def find_by_source_account_id(self, account_id):
        """
        Auslesen aller Ab-Buchungen eines durch Fremdschlüssel (Kontonr.) gegebenen Kontos.
        :param account_id: Schlüssel des zugehörigen Kontos.
        :return: Eine Liste mit Transaction-Objekten, die sämtliche Buchungen repräsentieren. Bei evtl. Exceptions wird
        ein partiell gefüllter oder ggf. auch leere Liste zurückgeliefert.
        """
        result = []
        cursor = self._cnx.cursor()
        try:
            command = "SELECT id, sourceAccount, targetAccount, amount, text, date FROM transactions " \
                      "WHERE sourceAccount={} ORDER BY id".format(account_id)
            cursor.execute(command)
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Transaktion-Objekt erstellt.
            for (id, source_account, target_account, amount, text, date) in tuples:
                transaction = Transaction()
                transaction.set_id(id)
                transaction.set_source_account(source_account)
                transaction.set_target_account(target_account)
                transaction.set_amount(amount)
                transaction.set_text(text)
                transaction.set_date(date)
                # Hinzufügen des neuen Objekts zur Liste
                result.append(transaction)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Liste zurückgeben
        return result

    def find_by_target_account_id(self, account_id):
        """
         Auslesen aller Ab-Buchungen eines durch Fremdschlüssel (Kontonr.) gegebenen Kontos.
         :param account_id: Schlüssel des zugehörigen Kontos.
         :return: Eine Liste mit Transaction-Objekten, die sämtliche Buchungen repräsentieren. Bei evtl. Exceptions wird
            ein partiell gefüllter oder ggf. auch leere Liste zurückgeliefert.
         """
        result = []
        cursor = self._cnx.cursor()
        try:
            command = "SELECT id, sourceAccount, targetAccount, amount, text, date FROM transactions " \
                      "WHERE targetAccount={} ORDER BY id".format(account_id)
            cursor.execute(command)
            tuples = cursor.fetchall()
            # Für jeden Eintrag im Suchergebnis wird nun ein Transaktion-Objekt erstellt.
            for (id, source_account, target_account, amount, text, date) in tuples:
                transaction = Transaction()
                transaction.set_id(id)
                transaction.set_source_account(source_account)
                transaction.set_target_account(target_account)
                transaction.set_amount(amount)
                transaction.set_text(text)
                transaction.set_date(date)
                # Hinzufügen des neuen Objekts zur Liste
                result.append(transaction)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Liste zurückgeben
        return result

    def find_by_key(self, key):
        """
        Suchen einer Buchung mit vorgegebener Buchungsnummer. Da diese eindeutig ist, wird genau ein Objekt
        zurückgegeben.
        :param key: id Primärschlüsselattribut (->DB)
        :return: Transaction-Objekt, das dem übergebenen Schlüssel entspricht, None bei nicht vorhandenem DB-Tupel.
        """
        cursor = self._cnx.cursor()
        try:
            # Statement ausfüllen und als Query an die DB schicken
            command = "SELECT id, sourceAccount, targetAccount, amount, text, date FROM transactions WHERE id={}"\
                .format(key)
            cursor.execute(command)
            tuples = cursor.fetchall()
            # Da id Primärschlüssel ist, kann max. nur ein Tupel zurückgegeben werden. Prüfe, ob ein Ergebnis vorliegt.
            (id, source_account, target_account, amount, text, date) = tuples[0]
            # Ergebnis-Tupel in Objekt umwandeln
            transaction = Transaction()
            transaction.set_id(id)
            transaction.set_source_account(source_account)
            transaction.set_target_account(target_account)
            transaction.set_amount(amount)
            transaction.set_text(text)
            transaction.set_date(date)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Rückgabe der Transaktion
        return transaction

    def insert(self, transaction):
        """
        Einfügen eines Transaction-Objekts in die Datenbank. Dabei wird auch der Primärschlüssel des übergebenen Objekts
        geprüft und ggf. berichtigt.
        :param transaction: das zu speichernde Objekt
        :return: das bereits übergebene Objekt, jedoch mit ggf. korrigierter id
        """
        cursor = self._cnx.cursor()
        try:
            # Zunächst schauen wir nach, welches der momentan höchste Primärschlüsselwert ist.
            cursor.execute("SELECT MAX(id) AS maxid FROM transactions ")
            tuples = cursor.fetchone()
            # Wenn wir etwas zurückerhalten, kann dies nur einzeilig sein
            (maxid) = tuples[0]
            # transaction erhält den bisher maximalen, nun um 1 inkrementierten Primärschlüssel.
            transaction.set_id(maxid + 1)
            # Jetzt erst erfolgt die tatsächliche Einfügeoperation
            command = "INSERT INTO transactions (id, sourceAccount, targetAccount, amount, text, date) " \
                      "VALUES ({},{},{},{},'{}','{}')"\
                .format(transaction.get_id(),
                        transaction.get_source_account(),
                        transaction.get_target_account(),
                        transaction.get_amount(),
                        transaction.get_text(),
                        transaction.get_date())
            cursor.execute(command)
        except IndexError as e:
            print(e)
            return None
        except sqlite3.OperationalError as e:
            print(e)
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        # Rückgabe, der evtl. korrigierten Buchung.
        return transaction

    def update(self, transaction):
        """
        Wiederholtes Schreiben eines Objekts in die Datenbank.
        :param transaction: das Objekt, das in die DB geschrieben werden soll
        :return: das als Parameter übergebene Objekt
        """
        cursor = self._cnx.cursor()
        try:
            command = "UPDATE transactions SET sourceAccount={}, targetAccount={}, amount={}, text='{}', date='{}' " \
                      "WHERE id={}".format(transaction.get_id(), transaction.get_source_account(),
                                           transaction.get_target_account(),
                                           transaction.get_amount(),
                                           transaction.get_text(),
                                           transaction.get_date())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()
        #  Um Analogie zu insert(Transaction t) zu wahren, geben wir t zurück
        return transaction

    def delete(self, transaction):
        """
        Löschen der Daten eines Transaction-Objekts aus der Datenbank.
        :param transaction: das aus der DB zu löschende "Objekt"
        :return: None
        """
        cursor = self._cnx.cursor()
        try:
            command = "DELETE FROM transactions WHERE id={}".format(transaction.get_id())
            cursor.execute(command)
        except IndexError:
            return None
        except sqlite3.OperationalError:
            return None
        finally:
            self._cnx.commit()
            cursor.close()


if __name__ == "__main__":
    mapper = TransactionMapper()
    result = mapper.find_all()
    for t in result:
        print(t)
