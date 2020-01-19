from tkinter import *
from client.forms.form import Form
from client.forms.transaction_form import TransactionForm


class AccountForm(Form):
    """
     Formular für Konten
     """
    def __init__(self, master, bi):
        super().__init__(master)

        self._master = master
        self.transaction_form = None

        # Referenz auf das BankInterface
        self.bi = bi

        # Die Werte der Eingabefelder werden hier gespeichert
        self.__id_text = IntVar()
        self.__owner_text = StringVar()
        self.__credit_line_text = DoubleVar()
        self.__balance_text = DoubleVar()

        # Setzen der Texte sowie der Eingabefelder
        self.header_label = Label(self.master, text="Übersicht Konto", bg='white')
        self.header_label.grid(row=0, column=0, sticky=W)

        self.kontonummer_label = Label(self.master, text="Kontonummer:", bg='white')
        self.kontonummer_entry = Entry(self.master, textvariable=self.__id_text, bg='white')
        self.kontonummer_entry.configure(state='readonly')
        self.kontonummer_label.grid(row=1, column=0, sticky=W)
        self.kontonummer_entry.grid(row=1, column=1)

        self.eigentuemer_label = Label(self.master, text="Eigentümmer:", bg='white')
        self.eigentuemer_entry = Entry(self.master, textvariable=self.__owner_text, bg='white')

        self.eigentuemer_entry.configure(state='readonly')
        self.eigentuemer_label.grid(row=2, column=0, sticky=W)
        self.eigentuemer_entry.grid(row=2, column=1)

        self.kreditlinie_label = Label(self.master, text="Kreditlinie:", bg='white')
        self.kreditlinie_entry = Entry(self.master, textvariable=self.__credit_line_text, bg='white')
        self.kreditlinie_entry.configure(state='readonly')
        self.kreditlinie_label.grid(row=3, column=0, sticky=W)
        self.kreditlinie_entry.grid(row=3, column=1)

        self.kontostand_label = Label(self.master, text="Kontostand:", bg='white')
        self.kontostand_entry = Entry(self.master, textvariable=self.__balance_text, bg='white', fg="green")
        self.kontostand_entry.configure(state='readonly')
        self.kontostand_label.grid(row=4, column=0, sticky=W)
        self.kontostand_entry.grid(row=4, column=1)

        # Die Buttons reagieren auf einen Klick. Durch einen Klick wird die Option command ausgeführt.
        self.delete_button = Button(self.master, text="Löschen", command=self._delete, bg='white')
        self.delete_button.grid(row=5, column=1, sticky=EW)

        self.transaction_button = Button(self.master, text="Überweisung", command=self.popup, bg='white')
        self.transaction_button.grid(row=5, column=0, sticky=W)

    def popup(self):
        """
        Erzeugt das Popup-Fenster und blockiert die Buttons des Kontoformulars
        :return:
        """
        self.transaction_form = TransactionForm(self)
        self.transaction_button["state"] = "disabled"
        self.delete_button["state"] = "disabled"
        # Es wird gewartet, bis das Überweisungsformular geschlossen wurde.
        self.master.wait_window(self.transaction_form._top)
        try:
            # Anschließend werden die Buttons wieder aktiviert
            self.transaction_button["state"] = "normal"
            self.delete_button["state"] = "normal"
            # und eine Überweisung durchgeführt, sofern der Kreditrahmen nicht überschritten wurde.
            self.bi.account_transaction(self.transaction_form._amount,
                                        self.transaction_form._target_account,
                                        self.transaction_form._reference)
        # Die Exception kann auftreten,
        # wenn in der Anwendung während des geöffneten Überweisungsformulars geklickt wird.
        except (AttributeError, TclError):
            pass

    def _delete(self):
        """
        löscht das Konto aus der Anwendung
        :return: None
        """
        self.bi.account_delete()

    def set_account(self, a):
        """
        Setzt das Konto in das Formular ein
        :param a: Das Konto
        :return: None
        """
        try:
            self.__id_text.set(a.get_id())
            self.update_balance(a)
            self.set_customer(a.get_owner())
            self.update_credit_line(a)
        # Wenn None beispielsweise übergeben wurde, werden die Felder geleert
        except AttributeError:
            pass#self.remove_account()

    def update_balance(self, a):
        """
        Setzt den aktuellen Kontostand in das Eingabefeld ein
        :param a: das Konto
        :return: None
        """
        try:
            self.__balance_text.set(round(a.get_balance(), 2))
            # Der Kontostand wird rot, wenn er in der Nähe des Kreditrahmens gelangt
            if a.is_balance_alert():
                self.kontostand_entry.configure(fg='red')
        except KeyError:
            self.__balance_text.set("")

    def update_credit_line(self, a):
        """
        Setzt den aktuellen Kreditrahmen in das Eingabefeld ein
        :param a: das Konto
        :return: None
        """
        try:
            self.__credit_line_text.set(a.get_credit_line())
        except KeyError:
            self.__credit_line_text.set(0.0)

    def remove_account(self):
        """
        Entfernt das aktuelle Konto aus dem Formular.
        Dabei werden Default-Werte in die Eingabemaske eingetragen.
        :return: None
        """
        self.__id_text.set(0)
        self.__owner_text.set("")
        self.__credit_line_text.set(0.0)
        self.__balance_text.set(0.0)

    def set_customer(self, c):
        """
        Setzt den Eigentümer in das Eingabefeld ein
        :param c: Der Kunde
        :return: None
        """
        try:
            self.__owner_text.set("{}, {}".format(c.get_last_name(), c.get_first_name()))
        except KeyError:
            self.__owner_text.set("")
