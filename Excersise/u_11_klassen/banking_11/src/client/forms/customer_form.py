from tkinter import *
from client.forms.form import Form


class CustomerForm(Form):
    """
    Formular für Kunden
    """
    def __init__(self, master, bi):
        super().__init__(master)
        # Referenz auf das BankInterface
        self.bi = bi

        # Die Werte der Eingabefelder werden hier gespeichert
        self.__id_text = IntVar()
        self.__first_name_text = StringVar()
        self.__last_name_text = StringVar()

        # Setzen der Texte sowie der Eingabefelder
        self.header_label = Label(self.master, text="Übersicht Kunde", bg='white')
        self.header_label.grid(row=0, column=0, sticky=W)

        self.first_name_label = Label(self.master, text="Vorname:", bg='white')
        self.first_name_entry = Entry(self.master, textvariable=self.__first_name_text, bg='white')
        self.first_name_label.grid(row=1, column=0, sticky=W)
        self.first_name_entry.grid(row=1, column=1)

        self.last_name_label = Label(self.master, text="Nachname:", bg='white')
        self.last_name_entry = Entry(self.master, textvariable=self.__last_name_text, bg='white')
        self.last_name_label.grid(row=2, column=0, sticky=W)
        self.last_name_entry.grid(row=2, column=1)

        self.id_label = Label(self.master, text="Id:", bg='white')
        self.id_entry = Entry(self.master, textvariable=self.__id_text, bg='white')
        self.id_entry.configure(state='readonly')
        self.id_label.grid(row=3, column=0, sticky=W)
        self.id_entry.grid(row=3, column=1)

        self.change_button = Button(self.master, text="Speichern", command=self.__update_customer, bg='white')
        self.change_button.grid(row=4, column=0, sticky=E)
        self.delete_button = Button(self.master, text="Löschen", command=self.__customer_delete, bg='white')
        self.delete_button.grid(row=4, column=1, sticky=EW)

    def set_customer(self, c):
        """
        Setzt den Kunden für das Formular
        :param: c: Kunde der betrachtet wird
        :return: None
        """
        try:
            # Die Informationen des Kunden werden in das Formular eingetragen
            self.update_id(c)
            self.update_first_name(c)
            self.update_last_name(c)
        # Wenn beispielsweise None übergeben wird, werden die Felder geleert
        except AttributeError:
            self.remove_customer()

    def update_id(self, c):
        """
        Setzt die Id des übergebenen Kunden in das Formular
        :param c: Der Kunde
        :return: None
        """
        try:
            self.__id_text.set(c.get_id())
        except KeyError:
            self.__id_text.set(0)

    def update_first_name(self, c):
        """
        Setzt den Vornamen des übergebenen Kunden in das Formular
        :param c: Der Kunde
        :return: None
        """
        try:
            self.__first_name_text.set(c.get_first_name())
        except KeyError:
            self.__first_name_text.set("")

    def update_last_name(self, c):
        """
        Setzt den Nachnamen des übergebenen Kunden in das Formular
        :param c: Der Kunde
        :return: None
        """
        try:
            self.__last_name_text.set(c.get_last_name())
        except KeyError:
            self.__last_name_text.set("")

    def remove_customer(self):
        """
        entfernt die Werte des Kunden aus dem Formular
        :return: None
        """
        self.__id_text.set(0)
        self.__first_name_text.set("")
        self.__last_name_text.set("")

    def get_id(self):
        """
        Liefert den aktuellen Wert aus dem Eingabefeld der Id zurück.
        :return: Id des Kunden
        """
        return self.id_entry.get()

    def get_last_name(self):
        """
        Liefert den aktuellen Wert aus dem Eingabefeld des Nachnamens zurück.
        :return: Nachname des Kunden
        """
        return self.last_name_entry.get()

    def get_first_name(self):
        """
        Liefert den aktuellen Wert aus dem Eingabefeld des Vornamens zurück.
        :return: Vorname des Kunden
        """
        return self.first_name_entry.get()

    def __update_customer(self):
        """
        Die Methode wird vom Button ausgelöst. Sie dient der Speicherung der Formulardaten in das Kundenobjekt und
        der Übertragung auf die Anwendung sowie die Datenbank.
        :return: None
        """
        self.bi.update_customer()

    def __customer_delete(self):
        """
        Die Methode wird vom Button ausgelöst. Sie dient der Löschung des aktuellen Kunden
        :return: None
        """
        self.bi.customer_delete()
