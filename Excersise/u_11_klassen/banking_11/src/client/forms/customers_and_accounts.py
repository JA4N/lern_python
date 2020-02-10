from tkinter.ttk import *


class CustomersAndAccounts(Treeview):
    """
    Klasse für den Treeview, der die Kunden mit den Konten verknüpft.
    """
    def __init__(self, master, bi):
        super().__init__(master, height=15, selectmode="extended")
        self.master = master
        # Referenz auf das Bankinterface
        self.bi = bi
        # Setzt in die erste Spalte die Überschrift
        self.heading('#0', text='Kunden', anchor='w')
        # Gibt die Breite der ersten Spalte an
        self.column('#0', width=200, anchor="c")
        # Wenn ein Linksklick durchgeführt wird, soll die Methode select_item() aus dem Bankinterface ausgeführt werden.
        self.bind('<ButtonRelease-1>', self.bi.select_item)
