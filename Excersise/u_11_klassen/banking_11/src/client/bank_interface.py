from tkinter import *
from server.bank_administration import BankAdministration
from client.forms.form import Form
from client.forms.account_form import AccountForm
from client.forms.customer_form import CustomerForm
from client.forms.customers_and_accounts import CustomersAndAccounts
from tkinter import messagebox


class BankInterface(Frame):
    """
    Die zentrale Servicestelle für Kontodienstleistungen.
    Hier werden alle Funktionaltitäten bereitgestellt.
    """
    def __init__(self, master):
        super().__init__(master, bg='white')
        # Referenz, um auf die Verarbeitungslogik zugreifen zu können.
        self._bank_administration = BankAdministration()

        # Aufbau der GUI-Elemente
        self.__master = master
        self.__master.grid_rowconfigure(0, weight=1)
        self.__master.grid_columnconfigure(0, weight=1)
        self.__master.grid_columnconfigure(1, weight=1)

        self.grid(sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.__left_frame = Form(self)
        self.__left_frame.grid(column=0, row=0, sticky='nw')
        self.__tree = CustomersAndAccounts(self.__left_frame, self)

        self.__right_frame = Form(self)
        self.__right_frame.grid(column=1, row=0, sticky='new')

        self.__menu = Menu(self.__master)
        self.__master.config(menu=self.__menu)

        # Vorhaltung aller Kunden und Konten
        self.__customers = {}
        self.__accounts = {}
        # Formulare
        self.__customer_form = None
        self.__account_form = None
        self.__transaction_form = None
        # Aktuell ausgewählter Kunde bzw. Konto
        self.__selected_account = None
        self.__selected_customer = None

    def customer_new(self):
        """
        Legt einen neuen Kunden in der Anwendung an.
        :return: None
        """
        # Zuerst wird ein vordefinierter Kunde erstellt
        c = self._bank_administration.create_customer("Mathilda", "Mustermann")
        # alle Widgets die sich auf dem rechten Frame befinden werden zunächst gelöscht.
        for widget in self.__right_frame.winfo_children():
            widget.destroy()
        # Anschließend wird der neue Kunde dem tree hinzugefügt
        item = self.insert_customer(c)
        self.__tree.focus(item)
        self.__selected_customer = c
        # Auf Basis des neuen Kunden wird die CustomerForm neu aufgebaut
        self.__create_customer_form()

    def customer_delete(self):
        """
        löscht einen Kunden aus der Anwendung
        :return: None
        """
        cur_focus = self.__tree.focus()
        try:
            # der ausgewählte Kunde wird aus der Liste der Kunden gesucht
            c = self.__customers[cur_focus]
            result = messagebox.askokcancel("Kunde löschen", "Möchten Sie den Kunden {}, {} wirklich löschen?"
                                            .format(c.get_last_name(), c.get_first_name()))
            # Wenn der "OK"-Button gedrückt wird.
            if result:
                # Die BankAdministration kümmert sich um das löschen des Kunden und dazugehörige Konten
                self._bank_administration.delete_customer(c)
                # Im Anschluss wird der Eintrag im Baum entfernt.
                self.__tree.delete(cur_focus)
                del self.__customers[cur_focus]
                self.__selected_customer = None
                self.__tree.selection_clear()
                # die CustomerForm wird zurückgesetzt und anschließend gelöscht
                self.__customer_form.set_customer(self.__selected_customer)
                for widget in self.__right_frame.winfo_children():
                    widget.destroy()
        # Wenn kein Kunde ausgewählt wurde
        except KeyError:
            messagebox.showerror("Fehler", "Kein Kunden ausgewält")

    def __build_customer_menu(self, menu):
        """
        Baut die Menüstruktur für den Kunden auf.
        :param menu: von der Anwendung
        :return: None
        """
        customer_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Kunde", menu=customer_menu)
        customer_menu.add_command(label="Neu", command=self.customer_new)
        customer_menu.add_command(label="Löschen", command=self.customer_delete)

    def __action_refresh(self):
        """
        Die bisherige baumstruktur wird komplett verworfen und anschließend neu aufgebaut.
        :return: None
        """
        self.__tree.delete(*self.__tree.get_children())
        self.__build_tree()

    def __print_all_accounts(self):
        """
        Gibt auf der Konsole alle Konten aus
        :return: None
        """
        for a in self.__accounts:
            self.__accounts.get(a).print_account_statement()

    def __action_exit(self):
        """
        Das Objekt der Bankanwendung wird zerstört und anschließend die Anwendung beendet.
        :return: None
        """
        self.destroy()
        sys.exit()

    def __build_action_menu(self, menu):
        """
        Baut die Menüstruktur für Aktionen auf, die nicht Kunden- oder Kontenspezifisch sind.
        :param menu: von der Anwendung
        :return: None
        """
        action_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Aktionen", menu=action_menu)
        action_menu.add_command(label="Aktualisierung", command=self.__action_refresh)
        action_menu.add_command(label="Alle Konten ausgeben", command=self.__print_all_accounts)
        action_menu.add_separator()
        action_menu.add_command(label="Beenden", command=self.__action_exit)

    def account_transaction(self, amount, target_account, reference):
        """
        Führt eine Transaktion auf einem Konto durch
        Es findet keine Prüfung statt, ob das angegebene Konto wirklich existiert oder nicht.
        :param amount: Der Betrag der überwiesen werden soll
        :param target_account: Das betroffene Konto
        :param reference: Der Buchungstext
        :return: None
        """
        try:
            # Prüfung ob der Betrag größer 0 ist, damit keine negativen Beträge überwiesen werden können.
            if int(amount) > 0:
                # Prüfung ob die Transaktion nicht die Kreditlinie überschreiten würde
                if not self.__selected_account.is_overdraw_amount(-1*float(amount)):
                    # Die BankAdministration erzeugt die Transaktion und führt diese durch
                    transaction = self._bank_administration.create_transaction_for(amount,
                                                                                   self.__selected_account.get_id(),
                                                                                   target_account,
                                                                                   reference)
                    # Der Kontostand des Kontos wird aktualisiert

                    new_amount = self._bank_administration.get_balance_of_account(self.__selected_account)
                    self.__selected_account.set_balance(new_amount)
                    self.__selected_account.add_transaction(transaction)
                    self.__update_account()
                else:
                    messagebox.showerror("Fehler", "Überschreitung der Kreditlinie!")
            else:
                messagebox.showerror("Fehler", "Negative Beträge können nicht überwiesen werden!")
        except AttributeError:
            messagebox.showerror("Fehler", "Kein Konto ausgewält")
        except (TypeError, ValueError):
            messagebox.showerror("Fehler", "Ungültige Eingabe")

    def __update_account(self):
        """
        Aktualisiert das Konto
        :return: None
        """
        cur_focus = self.__tree.focus()
        self.__accounts[cur_focus] = self.__selected_account
        self.__account_form.set_account(self.__selected_account)

    def update_customer(self):
        """
        Aktualisiert den Kunden
        :return: None
        """
        try:
            cur_focus = self.__tree.focus()
            # Die Änderungen werden auf den ausgewählten Kunden übernommen
            self.__selected_customer.set_first_name(self.__customer_form.get_first_name())
            self.__selected_customer.set_last_name(self.__customer_form.get_last_name())
            self.__selected_customer.set_id(self.__customer_form.get_id())
            # Die Änderungen werden gespeichert
            self._bank_administration.save_customer(self.__selected_customer)
            # Der Baum wird ebenfalls aktualisiert
            self.__customers[cur_focus] = self.__selected_customer
            self.__tree.item(cur_focus, text="{}, {}".format(self.__selected_customer.get_last_name(),
                                                             self.__selected_customer.get_first_name()))
        except KeyError:
            messagebox.showerror("Fehler", "Kein Kunden ausgewält")

    def __account_create(self):
        """
        Erzeugt ein neues Konto für einen Kunden
        :return:
        """
        try:
            cur_focus = self.__tree.focus()
            # Der Eigentümer wird ausgewählt
            owner = self.__customers[cur_focus]
            # Das Konto wird erzeugt
            a = self._bank_administration.create_account_for_customer(owner)
            for widget in self.__right_frame.winfo_children():
                widget.destroy()
            # Das Konto wird ausgewählt und in die Baumstruktur überführt
            self.__selected_account = a
            self.__create_account_form()
            item = self.insert_account(a, cur_focus)
            self.__tree.focus(item)
        except KeyError:
            messagebox.showerror("Fehler", "Kein Kunden ausgewält")

    def account_delete(self):
        """
        Löscht ein Konto
        :return: None
        """
        cur_focus = self.__tree.focus()
        try:
            a = self.__accounts[cur_focus]
            result = messagebox.askokcancel("Konto löschen", "Möchten Sie das Konto {} wirklich löschen?"
                                            .format(a.get_id()))
            if result:
                self.__tree.delete(cur_focus)
                del self.__accounts[cur_focus]
                self.__tree.selection_clear()
                self.__account_form.set_account(None)
                for widget in self.__right_frame.winfo_children():
                    widget.destroy()
                # Das Konto wird aus der Anwendung gelöscht
                self._bank_administration.delete_account(a)
        except KeyError:
            messagebox.showerror("Fehler", "Kein Konto ausgewält")

    def __account_calculate_interest(self):
        """
        Berechnet den Zinssatz eines Kontos.
        :return: None
        """
        try:
            messagebox.showinfo("Jahreszins", "Der Jahreszins beträgt: {0:.2f} EUR"
                                .format(self.__selected_account.get_interest()))
        except AttributeError:
            messagebox.showerror("Fehler", "Kein Konto ausgewält")

    def __account_print_statement(self):
        """
        Gibt auf der Konsole den Kontoauszug aus.
        :return: None
        """
        try:
            messagebox.showinfo("Kontoauszug", self.__selected_account.get_account_statement())
        except AttributeError:
            messagebox.showerror("Fehler", "Kein Konto ausgewält")

    def __build_account_menu(self, menu):
        """
        Baut die Menüstruktur für das Konto auf
        :param menu: von der Anwendung
        :return: None
        """
        account_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Konto", menu=account_menu)
        account_menu.add_command(label="Neues Konto erzeugen", command=self.__account_create)
        account_menu.add_command(label="Konto löschen", command=self.account_delete)
        account_menu.add_command(label="Zins berechnen", command=self.__account_calculate_interest)
        account_menu.add_command(label="Kontoauszug anzeigen", command=self.__account_print_statement)

    def __exercise_name_length(self):
        """
        Zeigt die Namenslänge eines Kunden an
        :return: None
        """
        try:
            messagebox.showinfo("Übunge Namenslänge", "Die Namenslänge von {} {} beträgt {}"
                                .format(self.__selected_customer.get_first_name(),
                                        self.__selected_customer.get_last_name(),
                                        len(self.__selected_customer.get_first_name()) +
                                        len(self.__selected_customer.get_last_name())
                                        ))
        except AttributeError:
            messagebox.showerror("Fehler", "Kein Kunde ausgewält")

    def __build_exercise_menu(self, menu):
        """
        Baut die Menüstruktur für die Übungen auf
        :param menu: von der Anwendung
        """
        exercise_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Übungen", menu=exercise_menu)
        exercise_menu.add_command(label="Namenslänge", command=self.__exercise_name_length)

    def select_item(self, a):
        """
        Wenn in der Baumstruktur ein Event erzeugt wird, im speziellen ein Linksklick (alle anderen werden ignoriert),
        wird diese Methode ausgeführt
        :param a: Das Klick-Event, es beinhaltet Informationen, wo der Klick passiert ist
        :return: None
        """
        cur_focus = self.__tree.focus()
        item = self.__tree.item(cur_focus)
        values = item['values']
        for widget in self.__right_frame.winfo_children():
            widget.destroy()
        try:
            # Anhand der Baumstruktur wird geprüft, ob ein Konto oder Kunde angeklickt wurde.
            # Entsprechend wird die jeweilige Form aufgerufen.
            if values[0] == "Account":
                self.__selected_account = self.__accounts.get(cur_focus)
                balance = self._bank_administration.get_balance_of_account(self.__selected_account)
                self.__selected_account.set_balance(balance)
                self.__create_account_form()
            if values[0] == "Customer":
                self.__selected_customer = self.__customers.get(cur_focus)
                self.__create_customer_form()
        except IndexError:
            """
            Tritt beispielsweise auf, wenn der ausgewählte Knoten gelöscht wird und 
            anschließend in dem Tree ein Click tätigt, ohne dabei einen Knoten auszuwählen.
            Sollte dies der Fall sein, soll er den "Fehler" übergehen
            """
            print(a)

    def __create_customer_form(self):
        """
        Erzeugt das Kundenformular
        :return: None
        """
        self.__customer_form = CustomerForm(self.__right_frame, self)
        self.__customer_form.set_customer(self.__selected_customer)

    def __create_account_form(self):
        """
        Erzeugt das Kontenformular
        :return: None
        """
        self.__account_form = AccountForm(self.__right_frame, self)
        self.__account_form.set_account(self.__selected_account)

    def create_and_show_gui(self):
        """
        Baut die Menüstruktur sowie den Baum auf.
        :return: None
        """
        self.__build_action_menu(self.__menu)
        self.__build_customer_menu(self.__menu)
        self.__build_account_menu(self.__menu)
        self.__build_exercise_menu(self.__menu)
        self.__build_tree()

    def __build_tree(self):
        """
        Aus der Datenbank werden über die BankAdministration alle Kunden sowie die dazugehörigen Konten abgerufen.
        Diese werden als Knoten in den Baum eingefügt.
        :return:
        """
        customers = self._bank_administration.get_all_customers()
        for c in customers:
            item = self.insert_customer(c)
            accounts = self._bank_administration.get_accounts_of_customer(c)
            for a in accounts:
                a.set_owner(c)
                a.set_balance(self._bank_administration.get_balance_of_account(a))
                self.insert_account(a, item)
        self.__tree.grid()

    def insert_customer(self, c):
        """
        Fügt einen Kunden dem Baum hinzu
        :param c: Der Kunde, der hinzugefügt werden soll
        :return: item: Index des erzeugten Knoten, wird benötigt, um die Konten anschließend korrekt zu platzieren.
        """
        item = self.__tree.insert("", "end",
                                  text="{}, {}".format(c.get_last_name(), c.get_first_name()),
                                  value=["Customer", c.get_id(), c.get_first_name(), c.get_last_name()])
        self.__customers[item] = c
        return item

    def insert_account(self, a, parent):
        """
        Fügt ein Konto dem Baum hinzu
        :param a: das Konto, das hinzugefügt werden soll
        :param parent: Der Elternknoten (hier: der Kunde)
        :return: None
        """
        item = self.__tree.insert(parent, 0, a.get_id(),
                                  text="Konto: {}".format(a.get_id()),
                                  value=["Account", a.get_id()])
        self.__accounts[item] = a
        return item


def run():
    """
    Führt die Anwendung aus
    :return: None
    """
    root = Tk()
    root.title('Bankanwendung')
    root.geometry('{}x{}'.format(460, 330))
    root.resizable(width=False, height=False)
    bi = BankInterface(root)
    bi.create_and_show_gui()
    mainloop()


if __name__ == "__main__":
    run()
