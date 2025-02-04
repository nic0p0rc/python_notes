import tkinter as tk
from tkinter import messagebox, mainloop

root = tk.Tk()
root.withdraw()
messagebox.showinfo("informazione", "Questa è una finestra di dialogo informativo")
messagebox.showwarning("Attenzione!", "Questa finestra ti mette in guardia")
messagebox.showerror("Errore", "Questa è una finestra di errore")

risposta = messagebox.askquestion("Domanda", "Vuoi continuare?")
if risposta == "yes":
    print("hai risposto si")
else:
    print("hai risposto no")

messagebox.askokcancel("Prova","Vuoi procedere?")
messagebox.askretrycancel("Prova","Riprovare?")

if messagebox.askyesno("prova", "si e no") == True:
    print("hai risposto si")
else:
    print("hai risposto no")


