from tkinter import *


class TransactionForm:
    """
    Formular für Überweisungen
    """
    def __init__(self, master):
        self.__master = master
        # Erzeugung eines neuen Fensters
        self._top = Toplevel(master, bg='white')

        # Die Werte der Eingabefelder werden hier gespeichert
        self.__target_account_text = IntVar()
        self.__reference_text = StringVar()
        self.__amount_text = DoubleVar()
        self.__target_account_text.set(0)
        self.__reference_text.set("")
        self.__amount_text.set(0.0)

        # Setzen der Texte sowie der Eingabefelder
        self.__header_label = Label(self._top, text="Überweisungsformular", bg='white')
        self.__header_label.grid(row=0, column=0, sticky=W)

        self.__target_account_label = Label(self._top, text="Zielkonto:", bg='white')
        self.__target_account_entry = Entry(self._top, textvariable=self.__target_account_text, bg='white')
        self.__target_account_label.grid(row=1, column=0, sticky=W)
        self.__target_account_entry.grid(row=1, column=1)

        self.__reference_label = Label(self._top, text="Buchungstext:", bg='white')
        self.__reference_entry = Entry(self._top, textvariable=self.__reference_text, bg='white')
        self.__reference_label.grid(row=2, column=0, sticky=W)
        self.__reference_entry.grid(row=2, column=1)

        self.__amount_label = Label(self._top, text="Betrag:", bg='white')
        self.__amount_entry = Entry(self._top, textvariable=self.__amount_text, bg='white')
        self.__amount_label.grid(row=3, column=0, sticky=W)
        self.__amount_entry.grid(row=3, column=1)

        # Die Buttons reagieren auf einen Klick. Durch einen Klick wird die Option command ausgeführt.
        self.__transaction_button = Button(self._top, text="Ausführen", command=self.__transaction, bg='white')
        self.__transaction_button.grid(row=4, column=0, sticky=W)

        self.__cancel_button = Button(self._top, text="Abbrechen", command=self.__cleanup, bg='white')
        self.__cancel_button.grid(row=4, column=1, sticky=EW)

    def __cleanup(self):
        """
        Das Widget zerstört sich selber (hier: _top
        :return: None
        """
        self._top.destroy()

    def __transaction(self):
        """
        Bevor das Widget zerstört wird, werden die Eingaben der Textfelder in Variablen zwischengespeichert,
        die nicht zum Widget dazugehören. Dadurch kann im Anschluss noch auf die Werte zugegriffen werden.
        :return: None
        """
        self._amount = self.__amount_entry.get()
        self._reference = self.__reference_entry.get()
        self._target_account = self.__target_account_entry.get()
        self.__cleanup()
