from tkinter import *
from unittest.mock import right

from pywin.scintilla.view import command_reflectors


class Window():
    def __init__(self, parent):
        self.input_box = Entry(parent,
                               font=("Arial",50),
                               #show="*"
                               )#fa visualizzare solo * come fosse una password
        self.input_box.pack(side=LEFT)

        self.submit_button = Button(parent, text="submit", command=self.submit)
        self.submit_button.pack(side=RIGHT)

    def submit(self):
        frase = self.input_box.get()
        print(frase)

