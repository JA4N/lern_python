import tkinter as tk
from logging import root


class Application (tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there ["text"] = "Click me..."
        self.hi_there ["command"] = self.say_hello
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="Quit", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hello(selfself):
        print("Hello World!")

root = tk.Tk()
app = Application(master=root)
app.master.title('Hello...')
app.mainloop()