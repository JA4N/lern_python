import sqlite3
from abc import ABC, abstractmethod


class Mapper(ABC):
    """
    Abstrakte Basisklasse aller Mapper-Klassen
    """
    _cnx = None

    def __init__(self):
        super().__init__()
        self.__get_connection()

    def __get_connection(self):
        if self._cnx is None:
            try:
                self._cnx = sqlite3.connect("bank.db")
            except sqlite3.Error as e:
                print("Failed to connect to bank.db: ".format(e))
        return self._cnx

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_key(self, key):
        pass

    @abstractmethod
    def insert(self, object):
        pass

    @abstractmethod
    def update(self, object):
        pass

    @abstractmethod
    def delete(self, object):
        pass


