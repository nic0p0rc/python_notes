import tkinter as tk
from tkinter import mainloop


def on_select():
    print(f"opzione selezionata: {selected_option.get()}")

root = tk.Tk()
root.title("Esempio di radio button")
root.geometry("500x300+800+500")

etichetta = tk.Label(root, text = "Widget",
                     bg= "darkblue",
                     font=("Arial, 30"),
                     fg = "white",
                     width = 20,
                     pady = 30)

etichetta.pack()

selected_option = tk.StringVar()
radio1 = tk.Radiobutton(root, text = "opzione 1", variable = selected_option, value = "opzione 1", command = on_select())
radio2 = tk.Radiobutton(root, text = "opzione 2", variable = selected_option, value = "opzione 2", command = on_select())
radio3 = tk.Radiobutton(root, text = "opzione 3", variable = selected_option, value = "opzione 3", command = on_select())

radio1.pack(side = tk.LEFT, anchor = "s")
radio2.pack(side = tk.LEFT, anchor = "s")
radio3.pack(side = tk.LEFT, anchor = "s")

ceck1 = tk.Checkbutton(root, text = "opzione 1")
ceck2 = tk.Checkbutton(root, text = "opzione 2")
ceck3 = tk.Checkbutton(root, text = "opzione 3")

ceck1.pack(side = tk.LEFT)
ceck2.pack(side = tk.LEFT)
ceck3.pack(side = tk.LEFT)

selected_option.set("Nicolò")
root.mainloop()